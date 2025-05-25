sentence = input("Type something > \n")

for letter in sentence:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print('\033[32m', end='')
    print(letter, end='')
    print('\033[0m', end='')

