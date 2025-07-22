# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-2025)
    my_jar = Jar()
    assert my_jar._capacity == 12
    assert my_jar.size == 0
    my_jar = Jar(24)
    assert my_jar._capacity == 24
    assert my_jar.size == 0


def test_str():
    my_jar = Jar()
    my_jar.deposit(1)
    assert str(my_jar) == '🍪'
    my_jar = Jar(2000)
    my_jar.deposit(122)
    my_jar.withdraw(120)
    assert str(my_jar) == '🍪🍪'


def test_deposit():
    my_jar = Jar(10)
    my_jar.deposit(1)
    assert str(my_jar) == '🍪'
    with pytest.raises(ValueError):
        my_jar.deposit(2025)


def test_withdraw():
    my_jar = Jar(10)
    my_jar.deposit(10)
    my_jar.withdraw(9)
    assert str(my_jar) == '🍪'
    with pytest.raises(ValueError):
        my_jar.withdraw(2025)
