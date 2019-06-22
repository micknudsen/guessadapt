import argparse
import gzip

from guessadapt.core import count_adapters


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
