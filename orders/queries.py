INSERT_ORDER = "INSERT INTO orders (id, total, currency) VALUES (%s, %s, %s)"


def insert_order(cur, order_id, total, currency="USD"):
    cur.execute(INSERT_ORDER, (order_id, total, currency))
