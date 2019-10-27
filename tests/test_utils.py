import unittest

from guessadapt.utils import iterquads


class TestUtils(unittest.TestCase):

    def test_iterquads(self):
        itr = iter(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        self.assertEqual(list(iterquads(itr)), [('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H')])
