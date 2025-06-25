# Alireza Nejati
# Monday , May 26 , 2025

while True:
    try:
        Fraction = input('Fraction: ')
        Fraction_parts = Fraction.split('/')
        X = int(Fraction_parts[0])
        Y = int(Fraction_parts[1])
        result = X/Y
        result = round(result, 2)
        result = int(result * 100)
        if (result >= 99 and result <= 100):
            print('F')
            break
        elif (result <= 1):
            print('E')
            break
        elif (result < 99 and result > 1):
            result = str(result)
            print(result + '%')
            break
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
