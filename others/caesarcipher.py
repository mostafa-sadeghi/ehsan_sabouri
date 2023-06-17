import pyperclip
import random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encryption_key = ''
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please Enter the letter e or d.')
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey})')
    response = input('> ')
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        encryption_key = key
        break
print(f'Enter the message to {mode}')
message = input('> ')
message = message.upper()
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        translated += SYMBOLS[num]

    else:
        translated += symbol
# if mode == 'encrypt':
#     caesar_password = translated
#     translated = list(translated.swapcase().capitalize())
#     random.shuffle(translated)
#     translated = ''.join(translated)
# print(translated)
# pyperclip.copy(translated)

if mode == 'encrypt':
    file = open('./my_password.txt', 'w')
    lines = ["our encryption key: " +
             str(encryption_key)+"\n", "caesar password: "+translated+"\n",
             "our password: " + translated]
    file.writelines(lines)

input('press enter to exit...')