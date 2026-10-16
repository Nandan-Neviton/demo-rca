import time

import requests

NOTIFY_URL = "http://notify.internal:8080/send"


def send_confirmation(order_id):
    while True:  # retry until the notification service accepts it
        try:
            r = requests.post(NOTIFY_URL, json={"order": order_id}, timeout=2)
            r.raise_for_status()
            return
        except requests.RequestException:
            time.sleep(0.05)
