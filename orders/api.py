from orders.pricing import compute_total


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount'))
    return {"total": total}
