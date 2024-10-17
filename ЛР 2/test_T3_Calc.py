import unittest
import Calc
import T3


class TestStringMethods(unittest.TestCase):
    """Тестирование функций по расчету остатка количества атомов после полураспада вещества
    и функции калькулятора из 1 лабораторной при помощи unittest"""

    def test_polonium_210(self):
        self.assertEqual(T3.radioactive_funcs["Po_210"](100, 150), 99.9991305091834)

    def test_polonium_214(self):
        self.assertEqual(T3.radioactive_funcs["Po_214"](100, 150), 6.08666031138343e-281)

    def test_summ(self):
        self.assertEqual(Calc.calculate(5, 3, '+'), 8)

    def test_div(self):
        self.assertEqual(Calc.calculate(3, 3, '/'), 1)

    def test_mult(self):
        self.assertEqual(Calc.calculate(3, 9, '*'), 27)


if __name__ == '__main__':
    unittest.main()
