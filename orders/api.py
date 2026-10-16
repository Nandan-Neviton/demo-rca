from orders.pricing import compute_total
from orders.shipping import cheapest_rate


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    shipping = cheapest_rate(payload.get("parcel", {}))
    return {"total": total, "shipping": shipping}
