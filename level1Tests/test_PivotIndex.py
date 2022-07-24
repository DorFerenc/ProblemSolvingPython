import pytest
from Level1.PivotIndex import PivotIndexClass

@pytest.fixture
def my_temp():
    return PivotIndexClass()


def test1(my_temp):
    lst1 = my_temp.pivotIndex([1, 7, 3, 6, 5, 6])
    assert lst1 == 3


def test2(my_temp):
    lst2 = my_temp.pivotIndex([1, 2, 3])
    assert lst2 == -1


def test3(my_temp):
    lst3 = my_temp.pivotIndex([2, 1, -1])
    assert lst3 == 0

def test4(my_temp):
    lst3 = my_temp.pivotIndex([1, 7, 3, 6, 5, 6])
    assert lst3 == 3

