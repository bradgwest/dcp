"""Given an array of numbers, find the maximum sum of any contiguous subarray
of the array.
"""


def brute(arr):
    # time: O(n^3); space: O(1)
    max_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            max_sum = max(max_sum, sum(arr[i : j + 1]))
    return max_sum


assert brute([34, -50, 42, 14, -5, 86]) == 137
assert brute([-5, -1, -8, -9]) == 0


def kande(arr):
    # time: O(n); space; O(1)
    max_so_far, max_ending_here = 0, 0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


assert kande([34, -50, 42, 14, -5, 86]) == 137
assert kande([-5, -1, -8, -9]) == 0


def kande_general(arr, f):
    # f can be min or max
    sum_so_far, sum_ending_here = 0, 0
    for x in arr:
        sum_ending_here = f(x, sum_ending_here + x)
        sum_so_far = f(sum_so_far, sum_ending_here)
    return sum_so_far


def kande_wrapped(arr):
    """
    The trick here is that the maximum circular subarray is the sum of the
    array minus the minimum subarray.

    time: O(n); space: O(1)
    """
    min_subarray = kande_general(arr, min)
    max_subarray = kande_general(arr, max)
    wrapped_sum = sum(arr) - min_subarray
    return max(wrapped_sum, max_subarray)


assert kande_wrapped([34, -50, 42, 14, -5, 86]) == 171
assert kande_wrapped([8, -1, 3, 4]) == 15
assert kande_wrapped([-5, -1, -8, -9]) == 0
