import time
from random import randint
import matplotlib.pyplot as plt


def left_leaf(root):
    return root * 4

def right_leaf(root):
    return root + 1

def gen_bin_tree(height: int, root: int) -> dict:
    if height <= 0:
        return {}

    tree = {str(root): []}

    left_l = gen_bin_tree(height - 1, left_leaf(root))
    right_l = gen_bin_tree(height - 1, right_leaf(root))

    if left_l:
        tree[str(root)].append(left_l)
    if right_l:
        tree[str(root)].append(right_l)

    return tree

def gen_bin_it_tree(height: int, root: int) -> dict:
    if height <= 0:
        return {}

    tree = {str(root): []}
    stack = [(root, height)]

    while stack:
        current_root, current_height = stack.pop()

        if current_height > 0:
            left_value = left_leaf(current_root)
            right_value = right_leaf(current_root)

            if str(left_value) not in tree:
                tree[str(left_value)] = []
            if str(right_value) not in tree:
                tree[str(right_value)] = []

            tree[str(current_root)].append({str(left_value): []})
            tree[str(current_root)].append({str(right_value): []})

            stack.append((left_value, current_height - 1))
            stack.append((right_value, current_height - 1))

    return tree

def setup_data(n: int) -> list:
    data = []
    for _ in range(n):
        root = randint(0, 3)
        height = randint(0, 10)
        data.append((root, height))
    return data

def calculate_time(data, func) -> float:
    start_time = time.time()
    for root, height in data:
        func(height, root)
    end_time = time.time()
    return (end_time - start_time) / len(data)

def main():
    num_runs = 10
    max_list_length = 50
    step = 5
    list_lengths = range(step, max_list_length + 1, step)

    results_rec = []
    results_iter = []

    for n in list_lengths:
        total_time_rec = 0
        total_time_iter = 0
        for _ in range(num_runs):
            data = setup_data(n)
            total_time_rec += calculate_time(data, gen_bin_tree)
            total_time_iter += calculate_time(data, gen_bin_it_tree)

        average_time_rec = total_time_rec / num_runs
        average_time_iter = total_time_iter / num_runs
        results_rec.append(average_time_rec)
        results_iter.append(average_time_iter)
        print(
            f"List length {n}: Recursive - {average_time_rec:.6f} seconds, Iterative - {average_time_iter:.6f} seconds"
        )

    plt.plot(list_lengths, results_rec, label="Recursive")
    plt.plot(list_lengths, results_iter, label="Iterative")
    plt.xlabel("Number of Tree Generations")
    plt.ylabel("Time (seconds)")
    plt.title("Binary Tree Generation Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
