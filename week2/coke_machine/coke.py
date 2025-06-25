# Alireza Nejati (alirezanejatiz27@gamil.com)

price = 50

while (True):
    print('Amount Due: ' + str(price))
    input_coin = int(input('Insert Coin: '))
    if (input_coin == 25 or input_coin == 10 or input_coin == 5):
        price = price - input_coin
        if (price <= 0):
            change_owed_number = price * -1
            print('Change Owed: ' + str(change_owed_number))
            break
