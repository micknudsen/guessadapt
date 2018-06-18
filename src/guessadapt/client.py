import argparse
import gzip
import logging
import sys

from Bio import SeqIO
from collections import Counter

from guessadapt.exceptions import ParserError


logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)


def parse_adapter_list(adapter_list_file):
    """Returns dictionary with adapater sequences as keys and adapter names as values.

    The adapter list file must be tab-separated with two columns. The first (resp. second)
    column should contain the adapter sequence (resp. adapter name). For example:

    CTGTCTCTTATA	Nextera Transposase
    AGATCGGAAGAGC	Illumina TruSeq
    """
    result = {}
    with open(adapter_list_file, 'r') as handle:
        for line in handle.read().splitlines():
            parts = line.split('\t')
            if not len(parts) == 2:
                raise ParserError(message='The adapter list must be tab-separated with two columns.')
            sequence, name = parts
            result[sequence] = name
    return result


def count_adapters(fastq_file, adapter_list_file, sequence_limit):
    adapters = parse_adapter_list(adapter_list_file=adapter_list_file)
    adapter_counts = Counter()
    with gzip.open(fastq_file, 'rt') as handle:
        for n, record in enumerate(SeqIO.parse(handle, 'fastq'), start=1):
            if n > sequence_limit:
                break
            for adapter in adapters:
                if adapter in record.seq:
                    adapter_counts[adapter] += 1
    return adapter_counts


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--fastq_file', '-f', required=True)
    parser.add_argument('--adapter_list_file', '-a', required=True)
    parser.add_argument('--sequence_limit', '-n', type=int, required=True)

    args = parser.parse_args()

    try:
        adapters = parse_adapter_list(args.adapter_list_file)
    except ParserError as e:
        logging.error(e.message)
        sys.exit(1)

    adapter_counts = count_adapters(fastq_file=args.fastq_file,
                                    adapter_list_file=args.adapter_list_file,
                                    sequence_limit=args.sequence_limit)

    print(adapter_counts.most_common()[0][0])
