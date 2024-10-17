def foo():
  name = 'Ann'

  surname = 'Stepanova'

  patronymic = 'Andreevna'

  birthday = '20.04.2005'

  def inner_boo():

    return {
        'name': name,
        'surname': surname,
        'patronymic': patronymic,
        'birthday': birthday
    }

  return inner_boo


print(foo()())
