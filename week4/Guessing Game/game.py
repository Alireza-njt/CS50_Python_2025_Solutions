# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 18 , 2025

from random import randint

level = 2025

while True:
    try:
        level = int(input('Level:'))
        if (level <= 0):
            pass
        else:
            break
    except ValueError:
        pass

random_number = randint(1, level)

while True:
    try:
        guess_number = int(input('Guess:'))
        if (guess_number <= 0):
            pass
        else:
            if (guess_number > random_number):
                print('Too large!')
            elif (guess_number < random_number):
                print('Too small!')
            else:
                print('Just right!')
                break

    except ValueError:
        pass
