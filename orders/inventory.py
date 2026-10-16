import requests

INVENTORY_URL = "http://inventory.internal:8080"


def reserve(sku, qty):
    r = requests.post(f"{INVENTORY_URL}/reserve", json={"sku": sku, "qty": qty})  # no timeout
    r.raise_for_status()
    return r.json()
