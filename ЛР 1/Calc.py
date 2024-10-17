def calculate(a, b, operand):
    """
    Функция калькулятора

    Аргументы:
    a(float): Первое число
    b(float): Второе число
    operand(str): Операция вычислений

    Возвращает:
    float: Результат вычислений

    """
    if operand == '+':
        return a + b
    if operand == '-':
        return a - b
    if operand == '*':
        return a * b
    elif operand == '/':
        if b == 0:
            return 'Ошибка: на ноль делить нельзя'
        else:
            return a / b


def main():
    """
    Функция main

    Аргументы:
    num1(float): Первое число
    num2(float): Второе число
    operation(str): Операция вычислений

    Возвращает:

    str: распечатка функции calculate
    """

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