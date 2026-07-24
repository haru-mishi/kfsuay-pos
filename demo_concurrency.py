"""
Proof that concurrent orders can't oversell stock.

Fires N concurrent single-unit orders at a branch/item seeded with
INITIAL_STOCK units, then asserts:
  - exactly INITIAL_STOCK requests succeeded
  - every other request got a clean 409 (not a crash, not a double-sell)
  - the DB's final stock count matches (never negative, never wrong)

Run inside the app container so APP_URL/DATABASE_URL are already set:
    docker compose exec app python demo_concurrency.py
"""

import os
from concurrent.futures import ThreadPoolExecutor

import httpx
import psycopg

APP_URL = os.environ.get("APP_URL", "http://localhost:8000")
DATABASE_URL = os.environ["DATABASE_URL"]

BRANCH_ID = 1  # KFSuay Bangkok
ITEM_ID = 1  # ALL IN ONE BUCKET
INITIAL_STOCK = 10
CONCURRENT_REQUESTS = 30


def place_order(_):
    with httpx.Client(base_url=APP_URL, timeout=10) as client:
        resp = client.post(
            f"/branches/{BRANCH_ID}/orders",
            json={"item_id": ITEM_ID, "quantity": 1},
        )
        return resp.status_code


def main():
    with ThreadPoolExecutor(max_workers=CONCURRENT_REQUESTS) as pool:
        results = list(pool.map(place_order, range(CONCURRENT_REQUESTS)))

    succeeded = results.count(200)
    rejected = results.count(409)
    other = [r for r in results if r not in (200, 409)]

    print(f"requests sent: {CONCURRENT_REQUESTS}")
    print(f"succeeded (200): {succeeded}")
    print(f"rejected (409, out of stock): {rejected}")
    if other:
        print(f"unexpected status codes: {other}")

    with psycopg.connect(DATABASE_URL) as conn:
        row = conn.execute(
            "SELECT quantity_available FROM stock WHERE branch_id = %s AND item_id = %s",
            (BRANCH_ID, ITEM_ID),
        ).fetchone()
    final_stock = row[0]
    print(f"final stock in DB: {final_stock}")

    assert not other, f"unexpected status codes: {other}"
    assert succeeded == INITIAL_STOCK, f"expected {INITIAL_STOCK} successes, got {succeeded}"
    assert rejected == CONCURRENT_REQUESTS - INITIAL_STOCK
    assert final_stock == 0, f"stock should be exactly 0, got {final_stock}"

    print("PASS: no oversell under concurrent requests.")


if __name__ == "__main__":
    main()
