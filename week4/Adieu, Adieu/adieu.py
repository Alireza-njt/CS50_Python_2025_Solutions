# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

children_list = []

while True:
    try:
        children_list.append(input())

    except EOFError:
        break

print('Adieu, adieu, to ', end='')

if (len(children_list) == 1):
    print(children_list[0])
elif (len(children_list) == 2):
    print(children_list[0], ' and ', children_list[1], sep='')
else:
    for i in range(len(children_list)):
        if (i < len(children_list)-1):
            print(children_list[i], ', ', sep='', end='')
        else:
            print('and', children_list[i])
