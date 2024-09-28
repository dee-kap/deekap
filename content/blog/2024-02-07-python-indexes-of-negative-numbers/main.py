import unittest


def find_negative_indexes(numbers):
    indexes = [i for i, n in enumerate(numbers) if n < 0]
    return indexes


class TestFindNegativeIndexes(unittest.TestCase):
    def test_find_negative_indexes(self):
        self.assertEqual(find_negative_indexes([1, -2, 3, -4, 5]), [1, 3])
        self.assertEqual(find_negative_indexes([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_negative_indexes([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])
        self.assertEqual(find_negative_indexes([]), [])


if __name__ == "__main__":
    unittest.main()
