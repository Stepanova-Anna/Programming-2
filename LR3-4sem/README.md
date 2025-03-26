# Лабораторная работа 3
>Текст задания размещен по [ссылке](https://gist.github.com/nzhukov/7a22f1c0a9c9d89954e01b014ec3e1b4)

### Результат [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/lr3.py)

Необходимые библиотеки:

`sys`: Предоставляет доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором Python. Используется для доступа к `sys.stdout` (стандартный поток вывода) и `sys.stderr` (стандартный поток ошибок).

`functools`: Предоставляет инструменты для работы с функциями и вызываемыми объектами. Здесь используется functools.wraps для сохранения метаданных оборачиваемой функции.

`sqlite3`: Предоставляет интерфейс для работы с базами данных SQLite.

`json`: Предоставляет инструменты для работы с данными в формате JSON.

`datetime`: Предоставляет классы для работы с датой и временем.

Декоратор `trace`: Это декоратор, который оборачивает функцию и добавляет функциональность трассировки.
Эта функция собирает данные, создавая список случайных корней и высот для деревьев.


![Лабораторная работа 3. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/lr3.png)

**[Тесты](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/test_lr3.py)**

Этот код предполагает, что `handle` является объектом подключения к базе данных, и у него есть метод `cursor()`

![Лабораторная работа 3. Задание 2](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/test.png)

**[Задание с контекстным менеджером](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/copylab.py)**

![Лабораторная работа 3. Задание 3](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR3-4sem/logs.png)
