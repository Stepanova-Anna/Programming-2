def two_sum_hashed_all(lst, target):
    """ Возвращает список всех наборов индексов, сумма которых равна target с использованием хеш-таблицы. """
    num_to_indices = {}
    result = []

    for i, num in enumerate(lst):
        if num in num_to_indices:
            num_to_indices[num].append(i)
        else:
            num_to_indices[num] = [i]

    seen_pairs = set()

    for i, num in enumerate(lst):
        complement = target - num
        if complement in num_to_indices:
            for j in num_to_indices[complement]:
                if i < j and (i, j) not in seen_pairs:
                    result.append((i, j))
                    seen_pairs.add((i, j))

    return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

result = two_sum_hashed_all(lst, target)

print("two_sum_hashed_all:", result)
