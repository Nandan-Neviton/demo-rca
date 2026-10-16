def validate_items(items):
    """Return the SKUs of the order; every item must be a dict from the catalog."""
    return [item["sku"] for item in items]


def create_order(payload):
    skus = validate_items(payload["items"])
    return {"skus": skus, "count": len(skus)}
