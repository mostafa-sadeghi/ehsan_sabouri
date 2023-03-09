import random
NUMDIGITS = 3
MAXGUESSES = 10


def generateSecretNumber():
    # convert str to list
    digits = list('0123456789')
    random.shuffle(digits)
    # convert list to str
    sec_number = ''
    for i in range(NUMDIGITS):
        sec_number += digits[i]

    return sec_number


print(f'''Welcome to our game.
You have {MAXGUESSES} times to guess a nonrepeated {NUMDIGITS} digits number.
Hint        Meaning
Pico        You guess right digit but in wrong place.
Fermi       You guess right digit in right position.
Bagels      All digits are wrong.
''')

secret_number = generateSecretNumber()
print(f'you have {MAXGUESSES} times')

counter = 0

while counter < MAXGUESSES:
    print(f'guess number {counter + 1}')
    guess = ''
    while len(guess) != 3 or not guess.isdecimal():
        guess = input(
            f'enter your guess, guess must be {NUMDIGITS} digits number:> ')

    counter += 1

    # Todo call get Hint Function
