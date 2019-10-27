import unittest

from guessadapt.utils import iterquads


class TestUtils(unittest.TestCase):

    def test_iterquads(self):
        self.assertEqual(list(iterquads(list('ABCDEFGH'))), [list('ABCD'), list('EFGH')])
