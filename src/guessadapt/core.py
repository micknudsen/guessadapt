from collections import Counter
from typing import Iterator, List


def parse_fastq(stream: Iterator[str]) -> Iterator[str]:
    while True:
        try:
            _, sequence, _, _ = next(stream), next(stream), next(stream), next(stream)
            yield sequence.strip()
        except StopIteration:
            break


def count_adapters(stream: Iterator[str], adapters: List[str], limit: int = None) -> Counter:
    adapter_counts: Counter = Counter()
    for n, sequence in enumerate(parse_fastq(stream), start=1):
        if limit and n > limit:
            break
        for adapter in adapters:
            if adapter in sequence:
                adapter_counts[adapter] += 1
    return adapter_counts
