# Alireza Nejati (alirezanejatiz27@gamil.com)

sound = input()

words = sound.split()

for i in range(len(words) - 1):
    print(words[i] + '...', end='')

print(words[len(words) - 1])
