from orders.dbconn import query


def order_history(customer_id):
    """Return every order for a customer together with its line items."""
    orders = query("SELECT id, total FROM orders WHERE customer_id = %s", (customer_id,))
    history = []
    for o in orders:
        items = query("SELECT sku, qty FROM order_items WHERE order_id = %s", (o["id"],))  # one query per order
        history.append({"order": o, "items": items})
    return history
