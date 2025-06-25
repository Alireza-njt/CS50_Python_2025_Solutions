# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 18 , 2025


import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        show_right_answer_sw = False
        right_answer = X + Y
        for i in range(3):
            my_answer = int(input(f'{X} + {Y} = '))
            if (my_answer == right_answer):
                score -= -1
                break
            else:
                print("EEE")
            if i == 2:
                show_right_answer_sw = True
        if show_right_answer_sw:
            print(f'{X} + {Y} = {right_answer}')

    print(score)


def get_level():
    while True:
        try:
            level = int(input('Level:'))
            if (level >= 1 and level <= 3):
                return level
            else:
                pass

        except ValueError:
            pass


def generate_integer(level):
    if (level == 1):
        return random.randint(0, 9)
    elif (level == 2):
        return random.randint(10, 99)
    elif (level == 3):
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
