# Alireza Nejati (alirezanejatiz27@gmail.com)
# June 2025

import re
# import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers_list = ip.strip().split('.')
    if (len(numbers_list) == 4):
        for i in range(4):
            try:
                number = int(numbers_list[i])
                if (number < 0 or number > 255):
                    return False
            except ValueError:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
