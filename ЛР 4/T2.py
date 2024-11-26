
def two_sum_hashed(lst, target):
    """Находит индексы двух элементов, сумма которых равна target, с O(n) сложностью."""
    ind = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in ind:
            return (ind[complement], i)
        ind[num] = i
    return None

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

result = two_sum_hashed(lst, target)
print(result)

