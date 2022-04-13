"""You run an e-commerce website and want to record the last N order ids in a
log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be
    smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

from collections import deque


class Log:
    def __init__(self, n: int) -> None:
        """Log of up to N items implemented with a deque. In python, this is
        implemented as a double ended queue.

        runtime: record => O(1); get_last => worst case O(n)
        space: O(n)
        """
        self.n = n
        self._orders = deque(maxlen=n)

    def record(self, order_id):
        self._orders.append(order_id)

    def get_last(self, i):
        try:
            return self._orders[-i]
        except IndexError:
            return None


if __name__ == "__main__":
    log = Log(5)
    assert log.get_last(2) is None
    log.record(1)
    log.record(2)
    assert log.get_last(2) == 1
    assert log.get_last(1) == 2
    assert log.get_last(3) is None
    log.record(3)
    log.record(4)
    log.record(5)
    log.record(6)
    assert log.get_last(5) == 2
    assert log.get_last(1) == 6
