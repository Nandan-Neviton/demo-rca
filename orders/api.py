from orders.pricing import compute_total
from orders.audit_log import record


def create_order(payload):
    total = compute_total(payload['items'], payload.get('discount', 0))
    record({"event": "order_created", "total": total})
    return {"total": total}
