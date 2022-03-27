from typing import Any, Callable, Tuple


def harness(cases: Tuple[Any, ...], solution: Callable[[Any], Any], **kwargs):
    failures = 0
    for i, t in enumerate(cases):
        actual = solution(t, **kwargs)
        if actual != t.expected:
            print(f"Case {i} failed. {t} != {actual}")
            failures += 1

    if failures:
        print(f"{len(cases) - failures}/{len(cases)}")
    else:
        print("SUCCESS")
