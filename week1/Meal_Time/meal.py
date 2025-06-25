# Alireza Nejati (alirezanejatiz27@gamil.com)

def main():
    time = input('What time is it? ')
    time_float_version = convert(time)

    if (time_float_version >= 7.0 and time_float_version <= 8.0):
        print('breakfast time')
    elif (time_float_version >= 12.0 and time_float_version <= 13.0):
        print('lunch time')
    elif (time_float_version >= 18.0 and time_float_version <= 19.0):
        print('dinner time')


def convert(time):
    time_parts = time.split(':')
    hour = time_parts[0]
    minute = time_parts[1]
    hour = float(hour)
    minute = float(minute)
    result = hour
    minute = minute / 60
    result = result + minute
    return result


if __name__ == "__main__":
    main()
