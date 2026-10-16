import os

# Base URL of the payments service. Deployments are expected to set PAYMENTS_URL.
PAYMENTS_URL = os.environ.get("PAYMENTS_URL", "http://localhost:9000")
