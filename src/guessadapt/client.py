import argparse
import gzip
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


def main():

    parser = argparse.ArgumentParser()

    # If no adapters are specified by the user, the following
    # three sequences are used as default:
    #
    # Illumina:   AGATCGGAAGAGC
    # Small RNA:  TGGAATTCTCGG
    # Nextera:    CTGTCTCTTATA

    default_adapters = 'AGATCGGAAGAGC,TGGAATTCTCGG,CTGTCTCTTATA'

    parser.add_argument('fastq', help='path to input FASTQ file')
    parser.add_argument('--limit', '-n', type=int, required=False, help='maximal number of reads to consider')
    parser.add_argument('--adapters', '-a', required=False, default=default_adapters, help='commma-separated list of adapters (default: %(default)s)')

    args = parser.parse_args()

    with gzip.open(args.fastq, 'rt') as handle:
        adapter_counts = count_adapters(handle=handle,
                                        limit=args.limit,
                                        adapters=args.adapters.split(','))

    adapter, _ = adapter_counts.most_common()[0]

    print(adapter)
