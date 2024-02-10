import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply_by_two(input, expected):
    result = input * 2
    assert result == expected
