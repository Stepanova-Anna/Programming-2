def two_sum(lst, target):
    """Находит индексы двух элементов, сумма которых равна target, с O(n^2) сложностью"""
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                return (i, j)

    return None
