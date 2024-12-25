from T1 import (calculate)


def test_add():
    """Проверяет функцию calculate() на сложение чисел с помощью тестирования assert"""
    assert calculate(7, 5, '+') == 12

def test_sub():
    """Проверяет функцию calculate() на вычитание чисел с помощью тестирования assert"""
    assert calculate(20, 8, '-') == 12

def test_mult():
    """Проверяет функцию calculate() на умножение чисел с помощью тестирования assert"""
    assert calculate(3, 3, '*') == 9

def test_div():
    """Проверяет функцию calculate() на деление чисел с помощью тестирования assert"""
    assert calculate(44, 22, '/') == 2

def test_div_by_zero():
    """Проверяет функцию calculate() на деление на ноль"""
    assert calculate(5, 0, '/') == 'Ошибка: на ноль делить нельзя'

def test_invalid_operator():
    """Проверяет функцию calculate() на неверный оператор"""
    assert calculate(1, 2, '%') == 'Ошибка: неверный оператор'
