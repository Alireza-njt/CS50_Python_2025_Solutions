# Alireza Nejati (alirezanejatiz27@gamil.com)


def main():
    camel_case_word = input('camelCase: ')
    snake_case_word = []

    for i in range(len(camel_case_word)):
        letter_type = char_type(camel_case_word[i])
        if (letter_type == 2):
            snake_case_word.append('_')
        snake_case_word.append(camel_case_word[i].lower())

    print('snake_case: ', end='')
    for i in range(len(snake_case_word) - 1):
        print(snake_case_word[i], end='')
    print(snake_case_word[len(snake_case_word) - 1])


def char_type(character):

    english_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letter in english_lowercase_letters:
        if (character == letter):
            return 1

    for letter in english_uppercase_letters:
        if (character == letter):
            return 2

    return -1


main()
