from collections import Counter
from typing import Iterator


class FastqRecord:

    def __init__(self, name: str, sequence: str) -> None:
        self.name = name
        self.sequence = sequence

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FastqRecord):
            return NotImplemented
        return self.name == other.name and self.sequence == other.sequence


class FastqParser:

    @classmethod
    def parse(cls, stream: Iterator[str]) -> Iterator[FastqRecord]:
        while True:
            try:
                name, sequence, _, _ = next(stream), next(stream), next(stream), next(stream)
                yield FastqRecord(name=name.strip()[1:], sequence=sequence.strip())
            except StopIteration:
                break


def count_adapters(handle, adapters, limit=None):
    """Counts number of occurrences in `handle` of each adapter
    in `adapters` list. The number of sequences to consider may be
    limited be specifying the optional `sequence_limit` parameter.

    :param handle: File handle for reading FASTQ file
    :param adapters list: List of adapters (strings)
    :param limit int: Maximal number of sequence to consider
    """
    parser = FastqParser()
    adapter_counts = Counter()
    for n, record in enumerate(parser.parse(handle), start=1):
        if limit and n > limit:
            break
        for adapter in adapters:
            if adapter in record.sequence:
                adapter_counts[adapter] += 1
    return adapter_counts
