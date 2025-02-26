def gen_bin_tree(height: int, root: int, left_leaf, right_leaf) -> dict:
    if height <= 0:
        return {}


    tree = {str(root): []}
    stack = [(root, height)]

    while stack:
        current_root, current_height = stack.pop()

        if current_height > 1:
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


if __name__ == '__main__':
    print(gen_bin_tree(4, 4, lambda x: x * 4, lambda x: x + 1))
