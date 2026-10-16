import requests
from requests.exceptions import JSONDecodeError  # added in requests 2.27


def fetch_rates():
    r = requests.get("http://rates.internal/v1/rates", timeout=5)
    try:
        return r.json()
    except JSONDecodeError:
        return {}
