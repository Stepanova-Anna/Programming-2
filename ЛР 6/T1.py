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


def main():
    """
    Функция main

    Возвращает:
        None: распечатка функции calculate
    """
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        operation = input('Введите необходимую операцию (+, -, *, /): ')

        if operation not in ('+', '-', '/', '*'):
            raise ValueError('Ошибка, введена неверная операция')

        result = calculate(num1, num2, operation)
        print(result)

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f'Произошла непредвиденная ошибка: {str(e)}')


if __name__ == "__main__":
    main()
