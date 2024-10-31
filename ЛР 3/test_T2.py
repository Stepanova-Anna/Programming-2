import unittest
from T2 import calculate

class TestCalculator(unittest.TestCase):

    def test_medium(self):
        self.assertAlmostEqual(calculate('medium', 1, 2, 3), 2)

    def test_variance(self):
        self.assertAlmostEqual(calculate('variance', 1, 2, 3,), 1)

    def test_std_deviation(self):
        self.assertAlmostEqual(calculate('std_deviation', 2, 3, 4), 1)

    def test_median(self):
        self.assertEqual(calculate('median', 1, 2, 3), 2)

    def test_iqr(self):
        self.assertEqual(calculate('iqr', 2, 3, 4, 5), 2)

if __name__ == "__main__":
    unittest.main()



