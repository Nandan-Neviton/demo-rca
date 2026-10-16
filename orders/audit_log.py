import json

AUDIT_PATH = "/var/log/orders/audit.log"


def record(event):
    with open(AUDIT_PATH, "a") as f:  # appended forever, never rotated
        f.write(json.dumps(event) + "\n")
