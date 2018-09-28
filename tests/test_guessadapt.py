import unittest

from guessadapt.client import count_adapters


class TestGuessAdapt(unittest.TestCase):

    def test_count_adapters(self):

        default_adapters = ['AGATCGGAAGAGC' ,'TGGAATTCTCGG', 'CTGTCTCTTATA']

        adapter_counts = count_adapters(fastq='tests/test.fastq.gz',
                                        adapters=default_adapters)

        self.assertEqual(len(adapter_counts), 3)

        self.assertEqual(adapter_counts['AGATCGGAAGAGC'], 3)
        self.assertEqual(adapter_counts['TGGAATTCTCGG'], 2)
        self.assertEqual(adapter_counts['CTGTCTCTTATA'], 1)
