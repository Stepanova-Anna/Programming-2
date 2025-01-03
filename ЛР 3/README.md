# Лабораторная работа № 3. Задачи.
**1.1:** Модернизируйте калькулятор из задач 1.2 и 1.4 Лабораторной работы
№ 2. Добавьте к калькулятору такую настройку как точность вычислений, которая передаётся в виде keyword параметра tolerance со
значением по умолчанию 1e−6. На основе переданного значения этого
параметра извлеките с помощью вычислений порядок этого значения
(например 6 для 1e−6) в виде отдельной функции convert_precision,
вызываемой из calculate. Задокументируйте convert_precision и
дополните документацию к calculate в коде. Извлечённый порядок
используйте для округления итогового результата в функции calculate.
Покройте (напишите) дополнительными тестами convert_precision
и calculate в связи с появлением tolerance с помощью пакета pytest
или стандартных unittest Python по выбору

**Результат:**

![Лабораторная работа 3. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_1.png)

Сложности при извлечении порядка точности из значения tolerance, для осуществления используем функцию ```log10``` для получения порядка, ```abs``` - берется абсолютное значение, чтобы избежать проблем с отрицательными числами.

```
return abs(int(log10(1/tolerance)))
```
**Тесты:**

![Лабораторная работа 3. Задание 1.1](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_1test.png)
![Лабораторная работа 3. Задание 1.1](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_1test2.png)

---
**1.2:** Модернизируйте калькулятор из задачи 1.1. Добавьте переменное количество неименоманных аргументов (операндов, ∗args) после параметра action и перед keyword параметром tolerance. К списку
поддерживаемых действий добавьте вычисление таких величин как
среднее значение (medium), дисперсия (variance), стандартное отклонение (std_deviation), медиана (median, q2, второй квартиль) и межквартильный размах (q3 - q1, разница третьего и первого квартилей).
Покройте новые реализованные функции и функцию calculate дополнительными юнит-тестами.


**Результат:**

![Лабораторная работа 3. Задание 2](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_2.png)

Чтобы избежать неверных операций проверяем что в ```args``` содержится как минимум два элемента на старте функции ```calculate```
```
    if len(args) < 2:
        print("Ошибка: введите более одного числа")
        return main()
```

Также для некоторых команд изначально можно вычислить ```sr``` - среднее значение, ```n``` - количество элементов, а также отсортируем все аргументы, для выполнения статистических операций 
```
        sr = sum(args) / len(args)
        n = len(args)
        args = sorted(args)
```


**Тесты:**

![Лабораторная работа 3. Задание 1.1](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_2test.png)
![Лабораторная работа 3. Задание 1.1](https://github.com/Stepanova-Anna/Programming-2/blob/main/img/LR3_2test1.png)
