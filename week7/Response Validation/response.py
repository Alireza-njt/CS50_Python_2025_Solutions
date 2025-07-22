# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

import validators
input_email = input("What's your email address? ")
if validators.email(input_email):
    print("Valid")
else:
    print("Invalid")
