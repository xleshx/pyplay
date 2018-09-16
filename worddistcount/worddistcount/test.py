import unittest
from worddistcount import WordDistanceCounter


class TestStringMethods(unittest.TestCase):

    def test_basic(self):
        word_counter = WordDistanceCounter("test1.txt")
        self.assertEqual(2, word_counter.find_shortest_distance("motivation", "development"))


if __name__ == '__main__':
    unittest.main()
