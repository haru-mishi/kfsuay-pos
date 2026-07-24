import os

from fastapi import FastAPI, HTTPException
from psycopg_pool import ConnectionPool
from pydantic import BaseModel, Field

DATABASE_URL = os.environ["DATABASE_URL"]
pool = ConnectionPool(DATABASE_URL, min_size=1, max_size=10, open=True)

app = FastAPI(title="KFSuay POS (slice)")


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
