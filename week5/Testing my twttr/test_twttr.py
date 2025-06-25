# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

from twttr import shorten


def test_twttr():
    assert shorten("Alireza") == "lrz"
    assert shorten("Computer") == "Cmptr"
    assert shorten("$fifty-three") == "$ffty-thr"
    assert shorten("2025 dollars") == "2025 dllrs"
    assert shorten("$23.57") == "$23.57"
