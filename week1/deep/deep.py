# Alireza Nejati (alirezanejatiz27@gamil.com)

answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

answer = answer.lower()  # To convert all uppercase letters in a string to lowercase
answer = answer.strip()  # To remove spaces at the beginning and end of a string

if answer == '42' or answer == 'forty-two' or answer == 'forty two':
    print('Yes')
else:
    print('No')
