# Alireza Nejati (alirezanejatiz27@gamil.com)

text = input()
words = text.split()

for i in range(len(words) - 1):
    if (words[i]) == ':)':
        print('🙂 ', end='')
    elif (words[i]) == ':(':
        print('🙁 ', end='')
    else:
        print(words[i] + ' ', end='')

if (words[len(words) - 1]) == ':)':
    print('🙂')
elif (words[len(words) - 1]) == ':(':
    print('🙁')
else:
    print(words[i])
