# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

import re
# import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s_parts = s.split(' ')
    is_first_time_pm = True
    is_second_time_pm = True
    first_time_final_format = ''
    second_time_final_format = ''
    if (len(s_parts) == 5):
        if (s_parts[2] == 'to'):
            if s_parts[1] == 'AM':
                is_first_time_pm = False
            if s_parts[4] == 'AM':
                is_second_time_pm = False
            first_time_parts = s_parts[0].split(':')
            second_time_parts = s_parts[3].split(':')
            if (len(first_time_parts) == 1 or len(first_time_parts) == 2) and (len(second_time_parts) == 1 or len(second_time_parts) == 2):
                if len(first_time_parts) == 1:
                    if len(first_time_parts[0]) == 2 and first_time_parts[0][0] == '0':
                        raise ValueError
                    if int(first_time_parts[0]) > 12:
                        raise ValueError
                    h = int(first_time_parts[0])
                    if is_first_time_pm:
                        if h != 12:
                            h += 12
                        first_time_final_format = f'{h}:00'
                    else:
                        if h == 12:
                            h = 0
                        first_time_final_format = f'{h:02d}:00'
                elif len(first_time_parts) == 2:
                    if len(first_time_parts[0]) == 2 and first_time_parts[0][0] == '0':
                        raise ValueError
                    if int(first_time_parts[0]) > 12:
                        raise ValueError
                    if int(first_time_parts[1]) > 59:
                        raise ValueError
                    h = int(first_time_parts[0])
                    m = int(first_time_parts[1])
                    if is_first_time_pm:
                        if h != 12:
                            h += 12
                        first_time_final_format = f'{h}:{m:02d}'
                    else:
                        if h == 12:
                            h = 0
                        first_time_final_format = f'{h:02d}:{m:02d}'
                if len(second_time_parts) == 1:
                    if len(second_time_parts[0]) == 2 and second_time_parts[0][0] == '0':
                        raise ValueError
                    if int(second_time_parts[0]) > 12:
                        raise ValueError
                    h = int(second_time_parts[0])
                    if is_second_time_pm:
                        if h != 12:
                            h += 12
                        second_time_final_format = f'{h}:00'
                    else:
                        if h == 12:
                            h = 0
                        second_time_final_format = f'{h:02d}:00'
                elif len(second_time_parts) == 2:
                    if len(second_time_parts[0]) == 2 and second_time_parts[0][0] == '0':
                        raise ValueError
                    if int(second_time_parts[0]) > 12:
                        raise ValueError
                    if int(second_time_parts[1]) > 59:
                        raise ValueError
                    h = int(second_time_parts[0])
                    m = int(second_time_parts[1])
                    if is_second_time_pm:
                        if h != 12:
                            h += 12
                        second_time_final_format = f'{h}:{m:02d}'
                    else:
                        if h == 12:
                            h = 0
                        second_time_final_format = f'{h:02d}:{m:02d}'
                return f'{first_time_final_format} to {second_time_final_format}'
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
