import os

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from psycopg_pool import ConnectionPool
from pydantic import BaseModel, Field

DATABASE_URL = os.environ["DATABASE_URL"]
pool = ConnectionPool(DATABASE_URL, min_size=1, max_size=10, open=True)

app = FastAPI(title="KFSuay POS (slice)")
app.mount("/demo", StaticFiles(directory="demo", html=True), name="demo")


class OrderRequest(BaseModel):
    item_id: int
    quantity: int = Field(gt=0)


@app.post("/branches/{branch_id}/orders")
def place_order(branch_id: int, order: OrderRequest):
    with pool.connection() as conn:
        with conn.transaction():
            cur = conn.execute(
                "SELECT quantity_available FROM stock "
                "WHERE branch_id = %s AND item_id = %s FOR UPDATE",
                (branch_id, order.item_id),
            )
            row = cur.fetchone()
            if row is None:
                raise HTTPException(404, "branch/item not found")

            available = row[0]
            if available < order.quantity:
                raise HTTPException(409, "insufficient stock")

            conn.execute(
                "UPDATE stock SET quantity_available = quantity_available - %s "
                "WHERE branch_id = %s AND item_id = %s",
                (order.quantity, branch_id, order.item_id),
            )
            order_id = conn.execute(
                "INSERT INTO orders (branch_id, item_id, quantity) "
                "VALUES (%s, %s, %s) RETURNING id",
                (branch_id, order.item_id, order.quantity),
            ).fetchone()[0]

    return {"order_id": order_id, "remaining_stock": available - order.quantity}


@app.get("/branches/{branch_id}/items/{item_id}/stock")
def get_stock(branch_id: int, item_id: int):
    with pool.connection() as conn:
        row = conn.execute(
            "SELECT quantity_available FROM stock "
            "WHERE branch_id = %s AND item_id = %s",
            (branch_id, item_id),
        ).fetchone()
    if row is None:
        raise HTTPException(404, "branch/item not found")
    return {"quantity_available": row[0]}


@app.post("/admin/reset")
def reset_demo_stock():
    # ponytail: hardcoded to the one seeded demo row (Bangkok / ALL IN ONE
    # BUCKET) — this exists only to re-arm the concurrency demo for repeat
    # recordings, not as a general admin API.
    with pool.connection() as conn:
        conn.execute(
            "UPDATE stock SET quantity_available = 10 "
            "WHERE branch_id = 1 AND item_id = 1"
        )
    return {"status": "reset", "branch_id": 1, "item_id": 1, "quantity_available": 10}
