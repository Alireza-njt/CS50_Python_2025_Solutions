# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

import re
# import sys


def main():
    print(count(input("Text: ")))


def count(s):
    result = 0
    s_parts = s.split(' ')
    for p in s_parts:
        p = re.sub(r'[^a-zA-Z]', '', p)
        if p.lower() == 'um':
            result += 1
    return result


if __name__ == "__main__":
    main()
