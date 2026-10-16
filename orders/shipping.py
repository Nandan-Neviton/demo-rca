import requests

SHIPPING_URL = "https://api.shipfast.example.com/rates"


def cheapest_rate(parcel):
    data = requests.get(SHIPPING_URL, params=parcel, timeout=5).json()
    return min(r["amount"] for r in data["rates"])
