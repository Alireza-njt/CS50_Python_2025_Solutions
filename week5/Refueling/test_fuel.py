# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 25 , 2025

from fuel import convert, gauge
from pytest import raises


def test_convert():
    assert convert('33/100') == 33
    assert convert('25/50') == 50
    assert convert('1/4') == 25
    assert convert('9/20') == 45


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(82) == '82%'


def test_errors():
    with raises(ValueError):
        convert('999/9')
    with raises(ZeroDivisionError):
        convert('2025/0')
