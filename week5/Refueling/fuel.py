# Alireza Nejati (alirezanejatiz27@gmail.com)
# Wednesday , June 25 , 2025

def main():
    ...


def convert(fraction):
    fraction_parts = fraction.split('/')
    X = fraction_parts[0]
    Y = fraction_parts[1]
    X = int(X)
    Y = int(Y)
    if X > Y:
        raise ValueError
    if Y == 0:
        raise ZeroDivisionError
    result = X / Y
    result = round(result, 2)
    result = int(result * 100)
    return result


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        percentage = int(percentage)
        return f'{percentage}%'


if __name__ == "__main__":
    main()
