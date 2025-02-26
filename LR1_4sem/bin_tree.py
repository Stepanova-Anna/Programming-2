#Root = 4; height = 4, left_leaf = root * 4, right_leaf = root + 1

def gen_bin_tree(height: int, root: int, left_leaf, right_leaf) -> dict:
    if height <= 0:
        return {}

    tree = {str(root): []}

    left_l = gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf)
    right_l = gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)

    if left_l:
        tree[str(root)].append(left_l)
    if right_l:
        tree[str(root)].append(right_l)

    return tree


if __name__ == '__main__':
    print(gen_bin_tree(4, 4, lambda x: x * 4, lambda x: x + 1))




