import unittest
from sort_Array import sortArray

class TestAlgorithm(unittest.TestCase):

    def test_empty_array(self):
        """Test for empty array:"""
        self.assertEqual(sortArray([]), [])

    def test_single_element(self):
        """Test for array with one element:"""
        self.assertEqual(sortArray([1]), [1])

    def test_reverse_array(self):
        """Test for reverse-order array:"""
        self.assertEqual(sortArray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_repeating_numbers(self):
        """Test array with repeating elements:"""
        self.assertEqual(sortArray([5, 6, 3, 3, 6, 3, 7, 7, 8, 3, 8]), [3, 3, 3, 3, 5, 6, 6, 7, 7, 8, 8])


if __name__ == "__main__":
    unittest.main(verbosity=2)