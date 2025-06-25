# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025
# Bitcoin Usd price in 6/24/2025 , 5:42 PM , Tehran Time Zone = $105,090.4407

# CoinCap Dashboard ------->>> https://pro.coincap.io/dashboard

from sys import argv, exit
from requests import get, RequestException

my_api_key = "3865d03e0f98f805398e1183b06d6e02cc53b580ef2e9e2d58be6e3b0a9f01bb"

if len(argv) == 1:
    exit('Missing command-line argument')
elif len(argv) == 2:
    try:
        coins_number_string = argv[1]
        coins_number_float = float(argv[1])
        get_argumant = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + my_api_key
        request = get(get_argumant)
        BitCoin_information = request.json()
        data_dictionary = BitCoin_information["data"]
        BitCoin_USD_price = data_dictionary["priceUsd"]
        BitCoin_USD_price = float(BitCoin_USD_price)
        result = coins_number_float * BitCoin_USD_price
        print(f"${result:,.4f}")
    except RequestException:
        exit('Request Error !!!')
    except ValueError:
        exit('Command-line argument is not a number')
