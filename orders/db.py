import queue

POOL_SIZE = 5
_pool = queue.Queue(maxsize=POOL_SIZE)
for _i in range(POOL_SIZE):
    _pool.put(object())


def get_conn(timeout=30):
    """Borrow a connection; raises queue.Empty when the pool is exhausted."""
    return _pool.get(timeout=timeout)


def release(conn):
    _pool.put(conn)
