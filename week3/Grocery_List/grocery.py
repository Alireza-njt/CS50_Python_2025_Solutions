# Alireza Nejati
# Wednesday , May 28 , 2025

grocery_map = {}

while True:
    try:
        item = input()
        grocery_map[item] = grocery_map[item] + 1

    except EOFError:
        break

    except KeyError:
        grocery_map[item] = 1

sorted_grocery_map_keys = sorted(grocery_map)

for key in sorted_grocery_map_keys:
    value = str(grocery_map[key])
    key = key.upper()
    print(value + ' ' + key)
