import unittest
import Calc


class TestStringMethods(unittest.TestCase):

    def test_summ(self):
        self.assertEqual(Calc.calculate(5, 3, '+'), 8)

    def test_div(self):
        self.assertEqual(Calc.calculate(3, 3, '/'), 1)

    def test_mult(self):
        self.assertEqual(Calc.calculate(3, 9, '*'), 27)

if __name__ == '__main__':
  unittest.main()