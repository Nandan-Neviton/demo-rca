import time

_counter = {"n": 1000}


def next_order_number():
    n = _counter["n"]
    time.sleep(0)  # let other threads run
    _counter["n"] = n + 1
    return n
