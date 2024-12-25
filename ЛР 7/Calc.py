import json
import os

PARAMS = {'precision': 0.00001, 'dest': 'output.txt'}

def load_params(file="params.json"):
    global PARAMS
    try:
        with open(file, mode='r', errors='ignore') as f:
            try:
                loaded_params = json.load(f)
                PARAMS.update(loaded_params)
            except json.JSONDecodeError as e:
                raise ValueError(f"Ошибка при парсинге JSON: {e}") from e
    except FileNotFoundError:
        print(f"Файл параметров '{file}' не найден, используются значения по умолчанию")
    return PARAMS

def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    try:
        with open(file, mode='a', errors='ignore') as f:
            f.write(f"{action}: {args} = {result} \n")
    except PermissionError as e:
         raise Exception(f'Ошибка записи в файл {file}: {e}') from e


def calculate(a, b, operand):
    """
    Функция калькулятора
    Аргументы:
        a (float): Первое число
        b (float): Второе число
        operand (str): Операция вычислений
    Возвращает:
        float: Результат вычислений или str: сообщение об ошибке
    """
    try:
        if operand == '+':
            return a + b
        elif operand == '-':
            return a - b
        elif operand == '*':
            return a * b
        elif operand == '/':
            if b == 0:
                raise ValueError('Ошибка: на ноль делить нельзя')
            else:
                return a / b
        else:
            raise ValueError('Ошибка: неверный оператор')
    except ValueError as e:
        return str(e)


