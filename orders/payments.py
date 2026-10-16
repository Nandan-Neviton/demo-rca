import requests

from orders.config import PAYMENTS_URL


def charge(order_id, amount):
    r = requests.post(f"{PAYMENTS_URL}/charge", json={"order": order_id, "amount": amount}, timeout=5)
    r.raise_for_status()
    return r.json()
