from collections import Counter

from Bio import SeqIO


def count_adapters(handle, adapters, limit=None):
    """Counts number of occurrences in `handle` of each adapter
    in `adapters` list. The number of sequences to consider may be
    limited be specifying the optional `sequence_limit` parameter.

    :param handle: File handle for reading FASTQ file
    :param adapters list: List of adapters (strings)
    :param limit int: Maximal number of sequence to consider
    """
    adapter_counts = Counter()
    for n, record in enumerate(SeqIO.parse(handle, 'fastq'), start=1):
        if limit and n > limit:
            break
        for adapter in adapters:
            if adapter in record.seq:
                adapter_counts[adapter] += 1
    return adapter_counts