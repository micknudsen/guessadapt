# from collections import Counter
from typing import Iterator  # , List


# class FastqRecord:

#     def __init__(self, name: str, sequence: str) -> None:
#         self.name = name
#         self.sequence = sequence


class FastqParser:

    @classmethod
    def parse(cls, stream: Iterator[str]) -> Iterator[str]:
        while True:
            try:
                _, sequence, _, _ = next(stream), next(stream), next(stream), next(stream)
                yield sequence.strip()
            except StopIteration:
                break


# def count_adapters(stream: Iterator[str], adapters: List[str], limit: int = None) -> Counter:
#     parser = FastqParser()
#     adapter_counts: Counter = Counter()
#     for n, record in enumerate(parser.parse(stream), start=1):
#         if limit and n > limit:
#             break
#         for adapter in adapters:
#             if adapter in record.sequence:
#                 adapter_counts[adapter] += 1
#     return adapter_counts
