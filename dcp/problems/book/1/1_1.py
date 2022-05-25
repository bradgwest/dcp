"""Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the original
array except the one at i.
"""

import functools
import operator


def partial_product(arr):
    # time: O(n); space: O(n)
    p = functools.reduce(operator.mul, arr)
    for i, v in enumerate(arr):
        arr[i] = p / v

    return arr


def partial_product_no_div(arr):
    # time O(n); space: O(n)
    # prefixes[i] is the product of the elements in arr[:i]
    prefixes = [1] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            prefixes[i] = 1
        else:
            prefixes[i] = functools.reduce(operator.mul, arr[:i])

    # suffixes[i] is the product of the elements in arr[i+1:]
    suffixes = [1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        if i == len(arr) - 1:
            suffixes[-1] = 1
        else:
            suffixes[i] = functools.reduce(operator.mul, arr[i + 1 :])

    suffixes = list(suffixes)
    for i, _ in enumerate(arr):
        arr[i] = prefixes[i] * suffixes[i]

    return arr


assert partial_product([3, 2, 1]) == [2, 3, 6]
assert partial_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

partial_product_no_div([3, 2, 1])
assert partial_product_no_div([3, 2, 1]) == [2, 3, 6]
assert partial_product_no_div([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
