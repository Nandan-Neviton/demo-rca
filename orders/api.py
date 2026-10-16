from orders.pricing import compute_total
from orders.notify import send_confirmation


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    send_confirmation(payload.get("order_id"))
    return {"total": total}
