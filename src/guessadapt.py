import argparse
import gzip

from Bio import SeqIO


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--fastq_file', '-f', required=True)
    parser.add_argument('--adapter_list', '-a', required=True)
    parser.add_argument('--sequence_limit', '-n', type=int, required=True)

    args = parser.parse_args()

    with gzip.open(args.fastq_file, 'rt') as handle:
        for n, record in enumerate(SeqIO.parse(handle, 'fastq'), start=1):
            if n > args.sequence_limit:
                break
