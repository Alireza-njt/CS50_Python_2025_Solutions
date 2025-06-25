# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , June 24 , 2025

def main():
    greeting = input()
    print(value(greeting))


def value(greeting):
    Greeting = greeting.lower()  # To convert all uppercase letters in a string to lowercase
    Greeting = Greeting.strip()  # To remove spaces at the beginning and end of a string

    Greeting_words = Greeting.split()  # To separate string words and assign them to a list

    if (Greeting_words[0][0] == 'h' and (Greeting_words[0] == 'hello' or Greeting_words[0] == 'hello,')):
        return 0
    elif (Greeting_words[0][0] == 'h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
