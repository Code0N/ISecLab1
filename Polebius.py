from random import random


def getrandom(min, max):
    return int((max - min) * random() + min)


def tablegenerator():
    lettermas = 'abcdefghiklmnopqrstuvwxyz'
    table = [[0] * 5 for row in range(5)]  # Генерация пустой таблицы

    for y in range(5):
        for x in range(5):
            table[x][y] = lettermas[getrandom(0, len(lettermas))]
            lettermas = lettermas.replace(table[x][y], '')
    return table


def getstr(x, format='%02s'):
    return ''.join(format % i for i in x)


def printtable(table):
    print(' ' + getstr(range(1, 6)))
    for row in range(0, len(table)):
        print(str(row + 1) + getstr(table[row]))


def encrypt(table, string):
    encrypted = ''

    for symbol in string.lower():
        for row in range(len(table)):
            if symbol in table[row]:
                x = str((table[row].index(symbol) + 1))
                y = str(row + 1)
                encrypted += y + x

    return encrypted


def decrypt(table, numbers):
    decrypted = ''
    for index in range(0, len(numbers), 2):
        y = int(numbers[index]) - 1
        x = int(numbers[index + 1]) - 1
        decrypted += table[y][x]
    return decrypted


istable = tablegenerator()
printtable(istable)
plaintext = input("Введите открытый текст\n").lower().replace(' ', '')
encryptedtext = encrypt(istable, plaintext)
print('Исходный текст: ' + plaintext)
print('Зашифрованный текст: ' + encryptedtext)
print('Расшифрованный текст: ' + decrypt(istable, encryptedtext))