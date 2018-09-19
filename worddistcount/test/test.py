import unittest
from worddistcount import WordDistanceCounter, calculate_distance


class TestStringMethods(unittest.TestCase):

    def test_integration(self):
        """Basic integration test case with I/O op coverage"""
        word_counter = WordDistanceCounter("test_file.txt")
        self.assertEqual(2, word_counter.find_shortest_distance("motivation", "development"))

    def test_duplicates(self):
        """Unit test with duplicates"""
        text_with_duplicates = "ops ops dev dev qa ops"
        self.assertEqual(1, calculate_distance(text_with_duplicates, "dev", "ops"))

    def test_start_after_end(self):
        text_with_duplicates = "ops ops dev dev qa ops dev"
        self.assertEqual(1, calculate_distance(text_with_duplicates, "dev", "ops"))

    def test_case_insensitive(self):
        text_with_duplicates = "ops Ops dev deV qa ops dev"
        self.assertEqual(1, calculate_distance(text_with_duplicates, "Dev", "opS"))

    def test_punctuation_agnostic(self):
        text_with_duplicates = "ops. ops! !!dev dev. qa<<< ops!:( dev=+>"
        self.assertEqual(1, calculate_distance(text_with_duplicates, "Dev", "opS"))


if __name__ == '__main__':
    unittest.main()
