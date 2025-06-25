# Alireza Nejati
# Monday , May 26 , 2025

menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0

while True:
    try:
        order = input('Item: ').lower()
        price = menu[order]
        total = price + total
        if (total % 1 == 0.5 or total % 1 == 0):
            total_str = str(total)
            print('Total: $' + total_str + '0')
        else:
            total_str = str(total)
            print('Total: $' + total_str)
    except KeyError:
        if (order == ''):
            break
        else:
            pass
    except EOFError:
        exit(0)
