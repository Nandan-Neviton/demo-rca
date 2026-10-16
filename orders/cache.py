_price_cache = {}


def cached_quote(order_id, items):
    """Cache quote per order id to avoid recomputation."""
    if order_id not in _price_cache:
        _price_cache[order_id] = [dict(i, snapshot=bytes(1024 * 256)) for i in items]  # ~256KB per item, never evicted
    return _price_cache[order_id]
