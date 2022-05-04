"""This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

import heapq


def solution(intervals):
    """
    strategy: sort the intervals, greedily choose rooms

    runtime: O(n log n) to sort, O(n) to iterate => O(n log n)
    space: O(n)
    """
    # sort by start time
    intervals = sorted(intervals, key=lambda x: x[0])
    rooms = []

    result = 0
    # loop invariant: rooms contains all rooms currently in use
    for start, end in intervals:
        while rooms and start > rooms[0]:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)
        if len(rooms) > result:
            result = len(rooms)

    return result


intervals = [(30, 75), (0, 50), (60, 150)]
print(solution(intervals))

intervals = [(0, 10), (1, 12), (3, 9), (13, 14), (10, 11)]
print(solution(intervals))
