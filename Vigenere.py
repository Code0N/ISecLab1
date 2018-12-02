lettersmas = 'abcdefghijklmnopqrstuvwxyz'



def encdec(string, key, mode):
    processed = []  # Затем будет конвертировано в строку
    keyindex = 0
    key = key.lower()

    for symbol in string:
        num = lettersmas.find(symbol.lower())
        if num != -1:
            if mode:
                num += lettersmas.find(key[keyindex])
            elif not mode:
                num -= lettersmas.find(key[keyindex])

            num %= len(lettersmas)

            processed.append(lettersmas[num])

            keyindex += 1
            if keyindex == len(key):
                keyindex = 0
        else:
            processed.append(symbol)
    return ''.join(processed)


iskey = input("Введите ключевую фразу\n").replace(' ', '').lower()
message = input("Введите открытый текст\n").lower().replace(' ', '')
encryptedmessage = encdec(message, iskey, True)
print("Зашифрованное сообщение: " + encryptedmessage)
print("Расшифрованное сообщение: " + encdec(encryptedmessage, iskey, False))
