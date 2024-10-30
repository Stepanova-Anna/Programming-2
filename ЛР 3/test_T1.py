import unittest
from T1 import calculate
from T1 import convert_precision



class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(calculate(1.123456, 2.123456, '+', tolerance=1e-6), 3.246912)

    def test_sub(self):
        self.assertAlmostEqual(calculate(5.5, 2.5, '-', tolerance=1e-6), 3.0)

    def test_mult(self):
        self.assertAlmostEqual(calculate(2.0, 3.0, '*', tolerance=1e-6), 6.0)

    def test_div(self):
        self.assertAlmostEqual(calculate(7.0, 2.0, '/', tolerance=1e-6), 3.5)

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(1e-9), 9)


if __name__ == "__main__":
    unittest.main()