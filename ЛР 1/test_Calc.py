from Calc import calculate


def test_add():
    """Проверяет функцию calculate() на сложение чисел с помощью тестирования assert"""
    assert calculate(7, 5, '+') == 12
    return 'Тест прошел успешно'


def test_sub():
    """Проверяет функцию calculate() на вычитание чисел с помощью тестирования assert"""
    assert calculate(20, 8, '-') == 12
    return 'Тест прошел успешно'


def test_mult():
    """Проверяет функцию calculate() на умножение чисел с помощью тестирования assert"""
    assert calculate(3, 3, '*') == 9
    return 'Тест прошел успешно'


def test_div():
    """Проверяет функцию calculate() на деление чисел с помощью тестирования assert"""
    assert calculate(44, 22, '/') == 2
    return 'Тест прошел успешно'


if __name__ == "__main__":
    print(test_add())
    print(test_sub())
    print(test_mult())
    print(test_div())
