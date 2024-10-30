import logging
from math import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    def wrapper(a, b, operand, tolerance=1e-6):
        logging.info(f"Посчитать: {a} {operand} {b}")
        result = func(a, b, operand, tolerance)
        logging.info(f"Результат: {result}, точность {tolerance}")
        return result
    return wrapper

def convert_precision(tolerance):
    """
    Извлекает порядок точности из значения tolerance.

    Аргументы:
    tolerance (float): Значение точности.

    Возвращает:
    int: Порядок точности.
    """
    return abs(int(log10(1/tolerance)))


@log_decorator
def calculate(a, b, operand, tolerance = 1e-6):
    """
    Функция калькулятора

    Аргументы:
    a (float): Первое число
    b (float): Второе число
    operand (str): Операция вычислений
    tolerance (float): Точность вычислений (по умолчанию 1e-6)

    Возвращает:
    float: Результат вычислений с учетом заданной точности.
    """
    order = convert_precision(tolerance)

    if operand == '+':
        result = a + b
    elif operand == '-':
        result = a - b
    elif operand == '*':
        result = a * b
    elif operand == '/':
        if b == 0:
            return 'Ошибка: на ноль делить нельзя'
        else:
            result = a / b
    else:
        return 'Ошибка: неверная операция'

    return round(result, order)

def main():

    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    operation = str(input('Введите необходимую операцию (+, -, *, /): '))

    if operation not in ('+', '-', '/', '*'):
        print('Ошибка, введена неверная операция')
        main()

    else:
        return print(calculate(num1, num2, operation))

if __name__ == "__main__":
  main()