# Alireza Nejati (alirezanejatiz27@gamil.com)

# A, E, I, O, and U

text = input('Input: ')
output_list = []
for letter in text:
    letter_upper_case = letter.upper()
    if (letter_upper_case == 'A' or letter_upper_case == 'E' or letter_upper_case == 'I' or letter_upper_case == 'O' or letter_upper_case == 'U'):
        pass
    else:
        output_list.append(letter)

print('Output: ', end='')
for i in range(len(output_list)-1):
    print(output_list[i], end='')

print(output_list[len(output_list)-1])
