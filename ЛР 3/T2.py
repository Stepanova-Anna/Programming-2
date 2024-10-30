import logging
from math import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    def wrapper(operand, *args, tolerance=1e-6):
        logging.info(f"Посчитать: {operand} для {args}")
        result = func(operand, *args, tolerance=tolerance)
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
    return abs(int(log10(1 / tolerance)))

@log_decorator
def calculate(operand, *args, tolerance=1e-6):
    """
    Функция калькулятора

    Аргументы:
    operand (str): Операция вычислений
    *args (float): Числа для вычислений
    tolerance (float): Точность вычислений (по умолчанию 1e-6)

    Возвращает:
    float: Результат вычислений
    """
    if len(args) < 2:
        print("Ошибка: введите более одного числа")
        return main()
    else:
        order = convert_precision(tolerance)
        sr = sum(args) / len(args)
        n = len(args)
        args = sorted(args)

        if operand == '+':
            return round(sum(args), order)
        elif operand == '-':
            return round(args[0] - sum(args[1:]), order)
        elif operand == '*':
            mult = 1
            for num in args:
                mult *= num
            return round(mult, order)
        elif operand == '/':
            if 0 in args[1:]:
                return 'Ошибка: на ноль делить нельзя'
            result = args[0]
            for num in args[1:]:
                result /= num
            return round(result, order)
        elif operand == 'medium':
            return round(sr, order)
        elif operand == 'variance':
            var = sum((num - sr) ** 2 for num in args)
            return round((var / (n - 1)), order)
        elif operand == 'std_deviation':
            d = sum((num - sr) ** 2 for num in args)
            return round((d / (n - 1)) ** 0.5, order)
        elif operand == 'median':
            if n % 2 == 0:
                return round(((args[n // 2 - 1] + args[n // 2]) / 2), order)
            else:
                return round((args[n // 2]), order)
        elif operand == 'iqr':
            q1_index = int(n * 0.25)
            q3_index = int(n * 0.75)
            q1 = args[q1_index] if n % 4 == 0 else args[q1_index - 1]
            q3 = args[q3_index] if n % 4 == 0 else args[q3_index]
            return round((q3 - q1), order)
        else:
            return 'Ошибка: неверная операция'

def main():
    """
    Функция main

    Запрашивает у пользователя ввод чисел и операции,
    затем выводит результат вычислений.
    """
    operation = str(input('Введите необходимую операцию (+, -, *, /, medium, variance, std_deviation, median, iqr): '))
    numbers = input('Введите числа через пробел: ')
    num_list = list(map(float, numbers.split()))
    print(calculate(operation, *num_list))

if __name__ == "__main__":
    main()
