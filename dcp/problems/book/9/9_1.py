import heapq


def add(val, min_heap, max_heap):
    median = get_median(min_heap, max_heap)
    if median is None or val <= median:
        heapq.heappush(max_heap, -1 * val)
    else:
        heapq.heappush(min_heap, val)


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -1 * root)


def get_median(min_heap, max_heap):
    if not (min_heap or max_heap):
        return None

    if len(min_heap) > len(max_heap):
        return min_heap[0]

    if len(max_heap) > len(min_heap):
        return max_heap[0] * -1

    return (min_heap[0] + -1 * max_heap[0]) / 2


def running_median(stream):
    min_heap = []
    max_heap = []
    for val in stream:
        add(val, min_heap, max_heap)
        # print(min_heap)
        # print(max_heap)
        rebalance(min_heap, max_heap)
        # print(min_heap)
        # print(max_heap)
        yield get_median(min_heap, max_heap)


for x in running_median([2, 1, 5, 7, 2, 0, 5]):
    print(x)
