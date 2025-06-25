# Alireza Nejati (alirezanejatiz27@gamil.com)

Greeting = input('Greeting: ')

Greeting = Greeting.lower()  # To convert all uppercase letters in a string to lowercase
Greeting = Greeting.strip()  # To remove spaces at the beginning and end of a string

Greeting_words = Greeting.split()  # To separate string words and assign them to a list

if (Greeting_words[0][0] == 'h' and (Greeting_words[0] == 'hello' or Greeting_words[0] == 'hello,')):
    print('$0')
elif (Greeting_words[0][0] == 'h'):
    print('$20')
else:
    print('$100')
