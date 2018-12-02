CTOIDic = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
ITOCDic = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))


def encdec(text, key, mode):
    encrypted = ''
    for sym in text:
        if sym.isalpha():
            if mode:
                encrypted += ITOCDic[(CTOIDic[sym] + key) % 26]
            elif not mode:
                encrypted += ITOCDic[(CTOIDic[sym] - key) % 26]
        else:
            encrypted + sym
    return encrypted


texttoencode = input("Введите открытый текст\n").lower()
try:
    key = int(input("Введите ключ (число между 1 и 26 включительно)\n"))
    if (key < 1 and key > 26):
        raise ValueError
except:
    exit(1)
encryptedtext = encdec(texttoencode, key, True)
print("Зашифрованный текст")
print("================\n")
print(encryptedtext + '\n')
print("Расшифрованный текст")
print("================\n")
print(encdec(encryptedtext, key, False) + '\n')
