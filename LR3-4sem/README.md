# Лабораторная работа 3
>Текст задания размещен по [ссылке](https://gist.github.com/nzhukov/7a22f1c0a9c9d89954e01b014ec3e1b4)

### Результат [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/lr3.py)

Необходимые библиотеки:

`sys`: Предоставляет доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python. Используется для доступа к `sys.stdout` (стандартный поток вывода) и `sys.stderr` (стандартный поток ошибок).

`functools`: Предоставляет инструменты для работы с функциями и вызываемыми объектами. Здесь используется functools.wraps для сохранения метаданных оборачиваемой функции.

`sqlite3`: Предоставляет интерфейс для работы с базами данных SQLite.

`json`: Предоставляет инструменты для работы с данными в формате JSON.

`datetime`: Предоставляет классы для работы с датой и временем.

```
def setup_data(n: int) -> list:
    data = []
    for _ in range(n):
        root = randint(0, 3)
        height = randint(0, 10)
        data.append((root, height))
    return data
```
Эта функция собирает данные, создавая список случайных корней и высот для деревьев.
```
def calculate_time(data, func) -> float:
    start_time = time.time()
    for root, height in data:
        func(height, root)
    end_time = time.time()
    return (end_time - start_time) / len(data)
```
Функция замеряет, сколько времени требуется для выполнения переданной функции func для каждого набора данных, и возвращает среднее время на одну итерацию.


![Лабораторная работа 3. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/lr3.png)


![Лабораторная работа 3. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/test.png)

