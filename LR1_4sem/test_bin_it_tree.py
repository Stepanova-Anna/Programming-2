import unittest
from bin_it_tree import gen_bin_tree


class TestBinTreeGeneration(unittest.TestCase):
    def test_simple_case(self):

        left_leaf = lambda x: x * 4
        right_leaf = lambda x: x + 1


        expected_result = {'16': [], '4': [{'16': []}, {'5': []}], '5': []}


        self.assertEqual(gen_bin_tree(2, 4, left_leaf, right_leaf), expected_result)


if __name__ == '__main__':
    unittest.main()
