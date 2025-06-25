# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s_len = len(s)
    if (s_len < 2 or s_len > 6):
        return False
    for i in range(len(s)):
        if (char_type(s[i]) == -1):
            return False
        if (char_type(s[i]) == 3 and (i == 0 or i == 1)):
            return False
        if (i > 0):
            if ((char_type(s[i]) == 1 or char_type(s[i]) == 2) and char_type(s[i-1]) == 3):
                return False
            if ((char_type(s[i]) == 3) and s[i-1] == '0' and s[i] != '0'):
                return False
    return True


def char_type(character):

    english_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    for letter in english_lowercase_letters:
        if (character == letter):
            return 1

    for letter in english_uppercase_letters:
        if (character == letter):
            return 2

    for number in numbers:
        if (character == number):
            return 3

    return -1


if __name__ == "__main__":
    main()
