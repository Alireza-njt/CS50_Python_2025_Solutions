# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

from plates import is_valid


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_1():
    # ------------------------ False ------------------------
    assert is_valid('AlirezaNejati') == False
    assert is_valid('A') == False
    assert is_valid('b') == False
    # ------------------------ True ------------------------
    assert is_valid('Aa') == True
    assert is_valid('ANZ27') == True
    assert is_valid('AbCdEf') == True

# “All vanity plates must start with at least two letters.”
def test_2():
    # ------------------------ False ------------------------
    assert is_valid('2025') == False
    assert is_valid('o2') == False
    assert is_valid('A999') == False
    assert is_valid('z36') == False
    # ------------------------ True ------------------------
    assert is_valid('CS50') == True
    assert is_valid('AZ') == True
    assert is_valid('OO99') == True


# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_3():
    # ------------------------ False ------------------------
    assert is_valid('AAA22A') == False
    assert is_valid('wrv23q') == False
    assert is_valid('H2O') == False
    assert is_valid('Zz021') == False
    # ------------------------ True ------------------------
    assert is_valid('AAA222') == True
    assert is_valid('Oq2') == True
    assert is_valid('ZZZ123') == True
    assert is_valid('Aq99') == True
    assert is_valid('ll100') == True

# “No periods, spaces, or punctuation marks are allowed.”
def test_4():
    # ------------------------ False ------------------------
    assert is_valid('A5 3') == False
    assert is_valid('A.N.27') == False
    assert is_valid('a:z') == False
    assert is_valid('$4') == False
    assert is_valid('%99.99') == False
    assert is_valid('(*p)') == False
    assert is_valid('AA_1') == False
    assert is_valid('qu-2') == False
    # ------------------------ True ------------------------
    assert is_valid('kl32') == True
    assert is_valid('TTT32') == True
