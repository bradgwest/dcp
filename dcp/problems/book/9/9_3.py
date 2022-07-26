import heapq


def regular_numbers(n):
    twos = [2**i for i in range(n)]
    threes = [3**i for i in range(n)]
    fives = [5**i for i in range(n)]

    solutions = set()
    for i in twos:
        for j in threes:
            for k in fives:
                solutions.add(i * j * k)

    return sorted(solutions)


def reg_nums(n):
    solutions = [1]
    last = 0
    count = 0

    while count < n:
        val = heapq.heappop(solutions)
        if val <= last:
            # already seen this value
            continue

        yield val
        for factor in (2, 3, 5):
            heapq.heappush(solutions, val * factor)

        count += 1
        last = val


print(list(reg_nums(6)))
print("")
print(list(reg_nums(20)))
