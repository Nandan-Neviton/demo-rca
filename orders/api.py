from orders.pricing import compute_total
from orders.queries import insert_order


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    return {"total": total}


def save(cur, order_id, total):
    insert_order(cur, order_id, total)
