from orders.pricing import compute_total
from orders.counters import next_order_number


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    number = next_order_number()
    return {"total": total, "order_number": number}
