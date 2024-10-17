def calculate(a, b, operand):
  """
  Функция калкулятора
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
    Тестирование функции calculate с помощью assert
    """
    assert calculate(5, 3, '+') == 8, "Ошибка вычислений"
    assert calculate(8, 3, '-') == 0, "Ошибка вычислений"
    assert calculate(3, 3, '/') == 1, "Ошибка вычислений"

    test_calculator()
