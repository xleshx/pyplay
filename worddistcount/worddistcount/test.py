import unittest
from worddistcount import find_shortest_distance


class TestStringMethods(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(2, find_shortest_distance("We do value and reward motivation in our "
                                                   "development team. Development "
                                                   "is a key skill for a DevOp.", "motivation", "development"))


if __name__ == '__main__':
    unittest.main()
