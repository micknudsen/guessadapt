import unittest

from guessadapt.core import FastqParser

# from guessadapt.core import count_adapters


class TestFastqParser(unittest.TestCase):

    def setUp(self):
        self.stream = iter(['@SequenceA', 'ACGT', '+', 'IIII',
                            '@SequenceB', 'TCGA', '+', 'IIII'])

    def test_parser(self):
        records = list(FastqParser().parse(self.stream))
        self.assertEqual(records, ['ACGT', 'TCGA'])


# class TestCore(unittest.TestCase):

#     def test_count_adapters(self):

#         default_adapters = ['AGATCGGAAGAGC', 'TGGAATTCTCGG', 'CTGTCTCTTATA']

#         with open('tests/test.fastq', 'r') as handle:
#             adapter_counts = count_adapters(stream=handle,
#                                             adapters=default_adapters)

#         self.assertEqual(len(adapter_counts), 3)

#         self.assertEqual(adapter_counts['AGATCGGAAGAGC'], 3)
#         self.assertEqual(adapter_counts['TGGAATTCTCGG'], 2)
#         self.assertEqual(adapter_counts['CTGTCTCTTATA'], 1)

#     def test_count_adapters_with_limit(self):

#         default_adapters = ['AGATCGGAAGAGC', 'TGGAATTCTCGG', 'CTGTCTCTTATA']

#         with open('tests/test.fastq', 'r') as handle:
#             adapter_counts = count_adapters(stream=handle,
#                                             adapters=default_adapters,
#                                             limit=3)

#         self.assertEqual(len(adapter_counts), 1)

#         self.assertEqual(adapter_counts['AGATCGGAAGAGC'], 3)
