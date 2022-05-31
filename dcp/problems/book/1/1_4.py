"""Given an array of integers, return a new array where each element in the
new array is the number of smaller elements to the right of that element in the
original array.
"""

import bisect


def brute(arr):
    # time: O(n^2); space: O(n)
    result = [0] * len(arr)
    for i, x in enumerate(arr):
        for y in arr[i:]:
            if y < x:
                result[i] += 1
    return result


def num_smaller(arr):
    # time: O(nlogn); space: O(n)
    result = []
    # a sorted list of elements to the right
    seen = []

    for x in reversed(arr):
        # i is the insertion point in the sorted list of seen. i.e. seen[:i]
        # are all less than x, so i is the number of elements right of x in
        # arr that are smaller than x.
        i = bisect.bisect_left(seen, x)
        result.append(i)
        # sort seen, ensuring
        bisect.insort(seen, x)

    return list(reversed(result))


assert brute([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
assert num_smaller([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
