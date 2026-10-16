# orders-api
Small service that accepts customer orders (POST /orders), computes totals with optional discounts and charges them
through the payments service (env var PAYMENTS_URL, e.g. http://payments.internal:8080).
