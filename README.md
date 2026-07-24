# KFSuay POS (slice)

A minimal slice of a multi-branch restaurant POS: one endpoint that takes
concurrent orders against per-branch stock without overselling, using a
Postgres row lock (`SELECT ... FOR UPDATE`) inside a transaction.

See [`DESIGN.md`](./DESIGN.md) for the problem, the approach, and what's
roadmap vs. built.

## Run it

```
docker compose up --build
```

This starts Postgres (seeded via `init.sql`) and the API on
`http://localhost:8000`.

## Prove it works under concurrency

```
docker compose exec app python demo_concurrency.py
```

Fires 30 concurrent orders at a branch/item seeded with 10 units in
stock, and asserts exactly 10 succeed, the rest get `409`, and the DB's
final stock is exactly 0.

## API

```
POST /branches/{branch_id}/orders
{ "item_id": <int>, "quantity": <int> }
```

- `200` — order placed, returns `{ "order_id": ..., "remaining_stock": ... }`
- `409` — insufficient stock
- `404` — branch/item not found
