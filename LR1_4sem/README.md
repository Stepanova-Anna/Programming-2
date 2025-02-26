# Лабораторная работа 1. Построение бинарного дерева
> Разработайте программу на языке Python, которая будет строить бинарное дерево (дерево, в каждом узле которого может быть только два потомка). Отображение результата в виде словаря (как базовый вариант решения задания). Далее исследовать другие структуры, в том числе доступные в модуле collections в качестве контейнеров для хранения структуры бинарного дерева.
> 
> Необходимо реализовать рекурсивный и нерекурсивный вариант gen_bin_tree
Дерево должно обладать следующими свойствами:
> 
> В корне дерева (root) находится число, которое задает пользователь (индивидуально для студента).
Высота дерева (height) задается пользователем (индивидуально для студента).
Левый (left leaf) и правый потомок (right leaf) вычисляется с использованием алгоритмов
**Root = 4; height = 4, left_leaf = root*4, right_leaf = root+1**

### Рекурсивный метод: [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/bin_tree.py)

Для вывода создаем словарь, где ключом является строковое представление корня, а значением - пустой список (для хранения дочерних узлов)

```
    tree = {str(root): []}
```

Рекурсивные вызовы:

    ```
    left_child = gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf)
    right_child = gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    ```
    
Рекурсивно создаются левые и правые дочерние поддеревья для текущего узла. Функции `left_leaf` и `right_leaf` применяются к значению корня, чтобы получить значения для дочерних узлов
    
По завершении рекурсивных вызовов возвращается сгенерированное бинарное дерево в виде словаря
![Лабораторная работа 1. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/LR1_T1.png)

### Тест: [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/test_bin_tree.py)
Для удобства отдельно вычисляем значения `left_leaf`, `right_leaf` и `expected_result`

![Лабораторная работа 1. Задание 1](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/LR1_test_T1.png)

---

### Нерекурсивный метод: [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/bin_it_tree.py)

### Тест: [код](https://github.com/Stepanova-Anna/Programming-2/blob/main/LR1_4sem/test_bin_it_tree.py)
