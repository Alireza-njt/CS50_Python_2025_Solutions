# Alireza Nejati (alirezanejatiz27@gmail.com)
# Monday , July 21 , 2025

import re
# import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    format = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)".*?'
    if match := re.match(format, s):
        url = match.group(1).split("/")[-1]
        return f"https://youtu.be/{url}"
    return None


if __name__ == "__main__":
    main()
