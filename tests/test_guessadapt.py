import unittest

from guessadapt.core import count_adapters


class TestGuessAdapt(unittest.TestCase):

    def test_count_adapters(self):

        default_adapters = ['AGATCGGAAGAGC', 'TGGAATTCTCGG', 'CTGTCTCTTATA']

        with open('tests/test.fastq', 'r') as handle:
            adapter_counts = count_adapters(handle=handle,
                                            adapters=default_adapters)

        self.assertEqual(len(adapter_counts), 3)

        self.assertEqual(adapter_counts['AGATCGGAAGAGC'], 3)
        self.assertEqual(adapter_counts['TGGAATTCTCGG'], 2)
        self.assertEqual(adapter_counts['CTGTCTCTTATA'], 1)

    def test_count_adapters_with_limit(self):

        default_adapters = ['AGATCGGAAGAGC', 'TGGAATTCTCGG', 'CTGTCTCTTATA']

        with open('tests/test.fastq', 'r') as handle:
            adapter_counts = count_adapters(handle=handle,
                                            adapters=default_adapters,
                                            limit=3)

        self.assertEqual(len(adapter_counts), 1)

        self.assertEqual(adapter_counts['AGATCGGAAGAGC'], 3)
