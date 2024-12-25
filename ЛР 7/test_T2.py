import pytest
from sum_2 import two_sum


@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, (0, 6)),
    ([-1, -2, 3, -4, 5, -6, 7, -8, 9], -10, (1, 7)),
    ([1, 2], 3, (0, 1)),
    ([-10 ** 9, 10 ** 9], 0, (0, 1)),
    ([1, 2, 3, 2, 4], 4, (0, 2)),
    ([2, 2, 2, 2], 4, (0, 1)),
    ([1, 2, 3, 4, 5], 100, None),
    ([5, 5, 5, 5], 10, (0, 1)),
    ([1, 5, 10, 15], 25, (2, 3)),
    ([1, 2, 3, 4], 7, (2, 3))

])
def test_two_sum(lst, target, expected):
    result = two_sum(lst, target)
    if expected is None:
        assert result is None
    else:
        assert result is not None
        assert set(result) == set(expected)