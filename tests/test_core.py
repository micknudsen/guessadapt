import unittest

from guessadapt.core import count_adapters
from guessadapt.core import parse_fastq


class TestFastqParser(unittest.TestCase):

    def setUp(self):
        self.stream = iter(['@SequenceA', 'ACGT', '+', 'IIII',
                            '@SequenceB', 'TCGA', '+', 'IIII'])

    def test_parser(self):
        records = list(parse_fastq(self.stream))
        self.assertEqual(records, ['ACGT', 'TCGA'])


class TestCore(unittest.TestCase):

    def setUp(self):

        self.adapters = ['ACG', 'CGT', 'TTT']

        self.stream = iter(['@SequenceA', 'ACGT', '+', 'IIII',
                            '@SequenceB', 'CGTT', '+', 'IIII',
                            '@SequenceC', 'GACG', '+', 'IIII',
                            '@SequenceD', 'TTTC', '+', 'IIII',
                            '@SequenceE', 'TCGT', '+', 'IIII'])

    def test_count_adapters(self):

        counts = count_adapters(stream=self.stream, adapters=self.adapters)

        self.assertEqual(len(counts), 3)
        self.assertEqual(counts['ACG'], 2)
        self.assertEqual(counts['CGT'], 3)
        self.assertEqual(counts['TTT'], 1)

    def test_count_adapters_with_limit(self):

        counts = count_adapters(stream=self.stream, adapters=self.adapters, limit=3)

        self.assertEqual(len(counts), 2)
        self.assertEqual(counts['ACG'], 2)
        self.assertEqual(counts['CGT'], 2)
        self.assertEqual(counts['TTT'], 0)
