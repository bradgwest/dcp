from collections import deque


def f(arr, k):
    # time: O(n); space: O(k)
    n = len(arr)
    if n < k:
        raise ValueError(f"arr must contain at least {k} elements")

    d = deque()
    for i in range(k):
        while d and arr[i] > arr[d[-1]]:
            d.pop()
        d.append(i)

    for i in range(k, n):
        yield arr[d[0]]
        # get rid of old values
        while d and d[0] <= i - k:
            d.popleft()

        # pop values smaller than current max
        while d and arr[i] > arr[d[-1]]:
            d.pop()

        d.append(i)

    yield arr[d[0]]


assert list(f([10, 5, 2, 7, 8, 7], 3)) == [10, 7, 8, 8]
