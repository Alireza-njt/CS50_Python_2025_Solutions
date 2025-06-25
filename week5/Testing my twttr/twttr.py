# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

def main():
    input_word = input()
    print(shorten(input_word))


def shorten(word):
    result_word = ''
    for letter in word:
        letter_upper_case = letter.upper()
        if (letter_upper_case == 'A' or letter_upper_case == 'E' or letter_upper_case == 'I' or letter_upper_case == 'O' or letter_upper_case == 'U'):
            pass
        else:
            result_word = result_word + letter
    return result_word


if __name__ == "__main__":
    main()
