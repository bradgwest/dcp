import collections
import heapq


def compare_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])


def similarity(log, k):
    visitors = collections.defaultdict(set)
    for site, user in log:
        visitors[site].add(user)
    sites = list(visitors.keys())

    # min heap of similarity scores
    scores = []
    # Prime the heap
    for _ in range(k):
        heapq.heappush(scores, (0, ("", "")))

    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = compare_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(scores, (score, (sites[i], sites[j])))

    return scores


log = [
    ("google", 1),
    ("google", 3),
    ("google", 5),
    ("pets", 1),
    ("pets", 2),
    ("yahoo", 6),
    ("yahoo", 2),
    ("yahoo", 3),
    ("yahoo", 4),
    ("yahoo", 5),
    ("wiki", 4),
    ("wiki", 5),
    ("wiki", 6),
    ("wiki", 7),
    ("bing", 1),
    ("bing", 3),
    ("bing", 5),
    ("bing", 6),
]

print(similarity(log, 1))
