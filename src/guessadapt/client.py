import argparse
import gzip
import sys

from Bio import SeqIO
from collections import Counter


def count_adapters(fastq, adapters, limit=None):
    """Counts number of occurrences in `fastq` of each adapter
    in `adapters` list. The number of sequences to consider may be
    limited be specifying the optional `sequence_limit` parameter.

    :param fastq str: Path to FASTQ file
    :param adapters list: List of adapters (strings)
    :param limit int: Maximal number of sequence to consider
    """
    adapter_counts = Counter()
    with gzip.open(fastq, 'rt') as handle:
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

    parser.add_argument('--fastq', '-f', required=True)
    parser.add_argument('--limit', '-n', type=int, required=False)
    parser.add_argument('--adapters', '-a', type=str, required=False, default=default_adapters)

    args = parser.parse_args()

    adapter_counts = count_adapters(fastq=args.fastq,
                                    limit=args.limit,
                                    adapters=args.adapters.split(','))

    print(adapter_counts.most_common()[0][0])
