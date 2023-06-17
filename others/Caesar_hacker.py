import string
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ') # AOHD

SYMBOLS = string.ascii_uppercase

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol

    print(translated)

