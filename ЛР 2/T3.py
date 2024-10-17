from functools import partial

# Периоды полураспада в секундах
half_per = {
    "Po_210": 138.4 * 24 * 3600,
    "Po_214": 0.16,
}

radioactive_funcs = {"Po_210": None, "Po_214": None}


def decay_amount(N0: float, t: int, t1_2=None):
    """
    Функция закона полураспада

    Параметры:
    N0 (float): изначальное количества вещества
    t (int): некоторый момент времени
    t1_2 (NoneType): период полураспада вещества

    Возвращает:
    N(float): оставшееся количество атомов вещества
    """

    N = N0 * (1 / 2) ** (t / t1_2)

    # res = 'Масса радиоактивного вещества:' + str(t1_2)
    print(f'Масса радиоактивного вещества: {str(t1_2)} \nПериод полураспада {t1_2}, \nN0 = {N0}, t = {t} с')
    return N


f1 = partial(decay_amount, t1_2=half_per['Po_210'])
f2 = partial(decay_amount, t1_2=half_per['Po_214'])


def main():
    """
    Вызов каррирования функции
    Создан цикл по словарю с распечаткой на экране сколько вещества осталось от одного и того же N0 в момент времени t
    """

    N0 = 100
    t = 150

    radioactive_funcs["Po_210"] = f1
    radioactive_funcs["Po_214"] = f2

    for isotope, func in radioactive_funcs.items():
        result = func(N0, t)
        print(f'Изотоп: {isotope}, Остаток: {result}')


main()
