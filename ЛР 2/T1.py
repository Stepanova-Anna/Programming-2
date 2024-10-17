def foo():

  """
    Функция foo внешняя функция

    Аргументы:

    name (str): Имя
    surname (str): Фамилия
    patronymic (str): Отчество
    birthday (str): Дата рождения

    Возвращает:

    Внутреннюю функцию inner_boo
    """


  name = 'Ann'

  surname = 'Stepanova'

  patronymic = 'Andreevna'

  birthday = '20.04.2005'

  def inner_boo():
    """Функция inner_boo внутренняя функция
    Аргументы: None
    Возвращает: Словарь сo следующими ключами
    name (str): Имя
    surname (str): Фамилия
    patronymic (str): Отчество
    birthday (str): Дата рождения"""


    return {
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
        'birthday': birthday
    }

  return inner_boo

print(foo()())
