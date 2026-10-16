from orders.pricing import compute_total
from orders.reporting import order_history


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    return {"total": total}


def get_customer_orders(customer_id):
    return order_history(customer_id)
