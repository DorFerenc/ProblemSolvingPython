import pytest
from Level1.IsomorphicStrings import IsomorphicStringsClass

@pytest.fixture
def my_temp():
    return IsomorphicStringsClass()


def test1(my_temp):
    s = "egg"
    t = "add"
    epRes = True
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test2(my_temp):
    s = "foo"
    t = "bar"
    epRes = False
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test3(my_temp):
    s = "paper"
    t = "title"
    epRes = True
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test4(my_temp):
    s = "badc"
    t = "baba"
    epRes = False
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test5(my_temp):
    s = "egcd"
    t = "adfd"
    epRes = False
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test6(my_temp):
    s = "a"
    t = "a"
    epRes = True
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test7(my_temp):
    s = "abab"
    t = "baba"
    epRes = True
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes


def test8(my_temp):
    s = "bbbaaaba"
    t = "aaabbbba"
    epRes = False
    res = my_temp.isIsomorphic(s, t)
    assert res == epRes

