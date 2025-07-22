# Alireza Nejati (alirezanejatiz27@gmail.com)
# June 2025

from numb3rs import validate


def test_for_True_cases():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('1.2.3.4') == True
    assert validate('100.102.104.23') == True
    assert validate('000.43.43.56') == True


def test_for_False_cases():
    assert validate('512.512.512.512') == False
    assert validate('-1.-1.-1.-1') == False
    assert validate('101.999.888.777') == False


def test_for_False_cases_2():  # When Match Method Returns False
    assert validate('ALIREZAAAAAAA') == False
    assert validate('NYC.45.67.78') == False
    assert validate('1.2.3.LA') == False
    assert validate('2025.2026.2027.2028') == False
    assert validate('1000.1001.1004.1009') == False
    assert validate('101.1000.2000.3000') == False
    assert validate('') == False
    assert validate('22') == False
    assert validate('22.23') == False
    assert validate('22.23.24') == False
    assert validate('22.23.24.25.26') == False
    assert validate('....') == False
