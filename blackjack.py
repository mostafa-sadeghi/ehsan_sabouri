'''
Rules:
    Try to get as close to 21 without going over.
    King, Queen, J => 10
    A  =>  1 | 11
    cards 2 through 10  =>  2 - 10
    (H)   =>  take another card
    (S)   =>  stop taking cards
    on your first play, you can (D)ouble down to increase your bet.
    


'''
import random
import sys

# Setup the constants

HEARTS = chr(9829)
DIMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'


def main():
    print('''Rules:
    Try to get as close to 21 without going over.
    King, Queen, J => 10
    A  =>  1 | 11
    cards 2 through 10  =>  2 - 10
    (H)   =>  take another card
    (S)   =>  stop taking cards
    on your first play, you can (D)ouble down to increase your bet.''')

    money = 5000

    while True:
        if money <= 0:
            print("You lose...")
            print("Thank you for playing...")
            sys.exit()
        print('Money:', money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)

        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("bet increased")
                print("Bet:", bet)
            # todo add S and D moves


def getBet(maxBet):
    bet = input(f'How much do you bet? (1 - {maxBet}), or QUIT')
    if bet.lower().startswith('q'):
        print("thank you for playing!")
        sys.exit()
    bet = int(bet)
    if 1 <= bet <= maxBet:
        return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIMONDS, SPADES, CLUBS):
        for i in range(2, 11):
            deck.append((str(i), suit))
        for i in ('J', 'Q', 'K', 'A'):
            deck.append((i, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER')
        displayCards([BACKSIDE] + dealerHand[1:])

    print("PLAYER", getHandValue(dealerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    row = ['', '', '', '']
    for i, card in enumerate(cards):
        row[0] += ' ___  '
        if card == BACKSIDE:
            row[1] += '|## | '
            row[2] += '|###| '
            row[1] += '|_##| '
        else:
            rank, suit = card
            row[1] += f'|{rank.ljust(2)} |'
            row[2] += f'| {suit} |'
            row[3] += f'|_{rank.ljust(2)}_|'

    for r in row:
        print(r)


def getMove(playerHand, money):

    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble')

        move = input(', '.join(moves) + '> ').upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble' in moves:
            return move
