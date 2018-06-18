import argparse
import gzip
import logging
import sys

from Bio import SeqIO
from collections import Counter

from guessadapt.exceptions import ParserError


logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)


def parse_adapter_list(filename):
    """Returns dictionary with adapater sequences as keys and adapter names as values.

    The adapter list file must be tab-separated with two columns. The first (resp. second)
    column should contain the adapter sequence (resp. adapter name). For example:

    CTGTCTCTTATA	Nextera Transposase
    AGATCGGAAGAGC	Illumina TruSeq
    """
    result = {}
    with open(filename, 'r') as handle:
        for line in handle.read().splitlines():
            parts = line.split('\t')
            if not len(parts) == 2:
                raise ParserError(message='The adapter list must be tab-separated with two columns.')
            sequence, name = parts
            result[sequence] = name
    return result


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--fastq_file', '-f', required=True)
    parser.add_argument('--adapter_list', '-a', required=True)
    parser.add_argument('--sequence_limit', '-n', type=int, required=True)

    args = parser.parse_args()

    try:
        adapters = parse_adapter_list(args.adapter_list)
    except ParserError as e:
        logging.error(e.message)
        sys.exit(1)

    adapter_counts = Counter()

    with gzip.open(args.fastq_file, 'rt') as handle:
        for n, record in enumerate(SeqIO.parse(handle, 'fastq'), start=1):
            if n > args.sequence_limit:
                break
            for adapter in adapters:
                if adapter in record.seq:
                    adapter_counts[adapter] += 1

    print(adapter_counts.most_common()[0][0])
