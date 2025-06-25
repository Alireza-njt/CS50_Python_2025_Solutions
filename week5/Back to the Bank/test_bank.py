# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

from bank import value


def test_0_dollars():
    assert value('hello Alireza !') == 0
    assert value('hello, Alireza !') == 0
    assert value('hello, Alireza!') == 0
    assert value('HELLO AlIREzA!') == 0
    assert value(' hello Alireza ') == 0


def test_20_dollars():
    assert value('hi, Alireza !') == 20
    assert value('How are you Alireza ?') == 20
    assert value('Hey Alireza !') == 20
    assert value(' Hey Alireza ! ') == 20
    assert value('HOW ArE YoU AlIReZa ????') == 20


def test_100_dollars():
    assert value("What's Up Alireza ?!") == 100
    assert value("Good Morning Alireza :)") == 100
    assert value("Welcome!") == 100
    assert value(" Welcome! ") == 100
    assert value("WeLcoMe! ") == 100
