import pytest
from main import compare_rows


@pytest.mark.parametrize('row_1, row_2', [
    (12, '123'),
    ('12', 123),
    (12, 123),
])
def test__compare_rows__returns_0_if_some_row_is_not_string(row_1, row_2):
    assert compare_rows(row_1, row_2) == 0


def test__compare_rows__returns_1_if_rows_equal():
    same_string = 'string value'
    assert compare_rows(same_string, same_string) == 1


@pytest.mark.parametrize('row_1, row_2', [
    ('string', 'str'),
    ('learn longer', 'learn'),
])
def test__compare_rows__returns_2_if_first_longer_than_second(row_1, row_2):
    assert compare_rows(row_1, row_2) == 2


@pytest.mark.parametrize('row_1, row_2', [
    ('str', 'learn'),
    ('lear', 'learn'),
])
def test__compare_rows__returns_2_if_second_is_longer_and_equals_learn(row_1, row_2):
    assert compare_rows(row_1, row_2) == 3


@pytest.mark.parametrize('row_1, row_2', [
    ('string', 'string_longer'),
    ('learn', 'learn '),
])
def test__compare_rows__raises_if_second_is_longer_and_not_equals_learn(row_1, row_2):
    with pytest.raises(ValueError):
        compare_rows(row_1, row_2)
