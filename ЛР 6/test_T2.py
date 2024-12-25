import unittest
from T1 import calculate

class TestCalculateFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(1, 2, '+'), 3)
        self.assertEqual(calculate(-1, -1, '+'), -2)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 3, '-'), 2)
        self.assertEqual(calculate(3, 5, '-'), -2)

    def test_multiplication(self):
        self.assertEqual(calculate(3, 4, '*'), 12)
        self.assertEqual(calculate(-2, 5, '*'), -10)

    def test_division(self):
        self.assertEqual(calculate(10, 2, '/'), 5)
        self.assertEqual(calculate(5, 0, '/'), 'Ошибка: на ноль делить нельзя')

    def test_invalid_operator(self):
        self.assertEqual(calculate(1, 2, '%'), 'Ошибка: неверный оператор')

if __name__ == "__main__":
    unittest.main(verbosity=1)
