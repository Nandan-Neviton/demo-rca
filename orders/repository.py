from orders.db import get_conn, release


def save_order(order):
    conn = get_conn()
    if order["total"] <= 0:
        raise ValueError("order total must be positive")  # connection never released
    # ... INSERT using conn ...
    release(conn)
    return order
