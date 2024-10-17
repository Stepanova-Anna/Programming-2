import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_decorator(func):

  def wrapper(a, b, operand):
    # Логирование входных данных
    logging.info(f"Посчитать: {a} {operand} {b}")

    # Вызов оригинальной функции
    result = func(a, b, operand)

    # Логирование результата
    logging.info(f"Результат: {result}")

    return result

  return wrapper


@log_decorator
def calculate(a, b, operand):
  """
  Функция вычисления

  Параметры:
  a (int): Первое число
  b (int): Второе число
  operand (str): Операция над числами

  Возвращает:
  int: Результат вычиислений
  или str: сообщение об ошибке при делении на ноль

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


def test_calculator():
  """
  Функция для тестирования функции calculate

  Проверяет корректность выполнения операций сложения, вычитания,
  умножения и деления, а также обработку ошибок

  """
  assert calculate(5, 3, '+') == 8
  assert calculate(8, 3, '-') == 5
  assert calculate(7, 6, '*') == 42
  assert calculate(3, 3, '/') == 1


test_calculator()

