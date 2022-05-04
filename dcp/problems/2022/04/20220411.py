"""This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the
array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place
and you do not need to store the results. You can simply print them out as you
compute them.
"""

from collections import deque, namedtuple

from dcp import harness


def brute(nums, k):
    for i in range(len(nums) - k + 1):
        yield (max(nums[i : (i + k)]))


def solution(nums, k):
    # preprocess
    q = deque()
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            # while the queue has values and the last element in the queue is
            # less than the current number, remove the number
            q.pop()
        # Add the index of the largest number seen
        q.append(i)

    for i in range(k, len(nums)):
        yield nums[q[0]]
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
    yield nums[q[0]]


if __name__ == "__main__":
    tc = namedtuple("TestCase", "nums k expected")

    cases = (
        tc([10, 5, 2, 7, 8, 7], 3, [10, 7, 8, 8]),
        tc([2, 3, 4], 2, [3, 4]),
        tc([2, 5, 6, 4, 3], 2, [5, 6, 6, 4]),
    )
    harness(cases, lambda t: list(solution(t.nums, t.k)))
