import pytest
from Level1.RunningSum import RunningSumClass

@pytest.fixture
def my_rs():
    return RunningSumClass()


def test1TRY(my_rs):
    lst1 = my_rs.runningSum([1, 2, 3, 4])
    assert lst1 == [1, 3, 6, 10]


def test2LETS(my_rs):
    lst2 = my_rs.runningSum([1, 1, 1, 1, 1])
    assert lst2 == [1, 2, 3, 4, 5]


def test3WHY(my_rs):
    lst3 = my_rs.runningSum([3, 1, 2, 10, 1])
    assert lst3 == [3, 4, 6, 16, 17]
