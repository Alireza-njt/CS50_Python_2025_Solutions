# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

from working import convert
import pytest


def test_convert():
    assert convert("11:00 AM to 7:00 PM") == "11:00 to 19:00"
    assert convert("10 AM to 7 PM") == "10:00 to 19:00"
    assert convert("10:45 PM to 9:50 AM") == "22:45 to 09:50"
    assert convert("11 PM to 3 AM") == "23:00 to 03:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("8:60 AM to 11:60 PM")
    with pytest.raises(ValueError):
        convert("5:60 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("89:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("1 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
