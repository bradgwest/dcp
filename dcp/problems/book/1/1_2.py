"""Given an array of integers that are out of order, determine the bounds
of the smallest window that must be sorted in order for the entire array to
be sorted.
"""


def bounds_naive(arr):
    # time: O(n log n); space: O(n)
    s = sorted(arr)
    lower = None
    upper = None
    for i, _ in enumerate(arr):
        if lower is None and s[i] != arr[i]:
            lower = i

        if upper is None and s[-(i + 1)] != arr[-(i + 1)]:
            upper = len(arr) - i - 1

        if lower and upper:
            break

    return lower, upper


def bounds(arr):
    # time: O(n); space: O(n)
    lower, upper = None, None
    n = len(arr)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(arr[i], max_seen)
        if arr[i] < max_seen:
            upper = i

    for i in range(n - 1, -1, -1):
        min_seen = min(arr[i], min_seen)
        if arr[i] > min_seen:
            lower = i

    return lower, upper


assert bounds_naive([3, 7, 5, 6, 9]) == (1, 3)
assert bounds_naive([5, 4, 3, 2, 1]) == (0, 4)

assert bounds([3, 7, 5, 6, 9]) == (1, 3)
assert bounds([5, 4, 3, 2, 1]) == (0, 4)
