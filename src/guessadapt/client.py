import argparse
import gzip
import sys

from Bio import SeqIO
from collections import Counter


def count_adapters(fastq_file, adapters, sequence_limit=None):
    """Counts number of occurrences of each adapter in `adapters` list
    in the `fastq_file`. Number of sequences to consider may be limited
    using the optional `sequence_limit` parameter.

    :param fastq_file str: Path to FASTQ file
    :param adapters list: List of adapters (strings)
    :param sequence_limit int: Maximal number of sequence to consider
    """
    adapter_counts = Counter()
    with gzip.open(fastq_file, 'rt') as handle:
        for n, record in enumerate(SeqIO.parse(handle, 'fastq'), start=1):
            if sequence_limit and n > sequence_limit:
                break
            for adapter in adapters:
                if adapter in record.seq:
                    adapter_counts[adapter] += 1
    return adapter_counts


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--fastq_file', '-f', required=True)
    parser.add_argument('--sequence_limit', '-n', type=int, required=False)
    parser.add_argument('--adapters', '-a', type=str, required=False, default='CTGTCTCTTATA,AGATCGGAAGAGC')

    args = parser.parse_args()

    adapter_counts = count_adapters(fastq_file=args.fastq_file,
                                    sequence_limit=args.sequence_limit,
                                    adapters=args.adapters.split(','))

    print(adapter_counts.most_common()[0][0])
