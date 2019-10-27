from typing import Iterator, Tuple


def iterquads(itr: Iterator[str]) -> Iterator[Tuple[str, str, str, str]]:
    i = 0
    while True:
        try:
            yield next(itr), next(itr), next(itr), next(itr)
            i += 4
        except StopIteration:
            break
