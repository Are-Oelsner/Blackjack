# Author: Are Oelsner
# This is a single-deck blackjack simulation
import random

# Card object - defined as having a suit and a value
class Card:
    # Parameters are int value and string suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    # Print function
    def print(self):
        print('suit: ' + self.suit + ', value: ' + str(self.value))
    # Returns the value of the card
    def getValue(self):
        return self.value

# Deck object - stores a list of Card objects
class Deck:
    def __init__(self):
        self.deck = []
    # Generates a list of 52 cards in order
    def genDeck(self):
        for suit in ('hearts', 'spades', 'clubs', 'diamonds'):
            for value in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10):
                self.deck.append(Card(value, suit))
    # Prints contents of deck list using the Card class print function
    def printDeck(self):
        for cards in self.deck:
            cards.print()
        print(len(self.deck))

    # Shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Removes and returns the top card of the deck
    def draw(self):
        return self.deck.pop()


# Blackjack game code
def Blackjack():
    # Displays the game board by showing information available to the player
    # Show parameter reveals the Dealer's first card to the player when true
    def printHands(show):
        if show == True:
            print('Dealer\'s Hand: \t' + str(dcard1) + ', ' + str(dcard2) + ', ' + str(dcard3) +'  sum: ' + str((dcard1 + dcard2 + dcard3)))
            print('Your Hand: \t' + str(pcard1) + ', ' + str(pcard2) , end='')
            for cards in PlayerHand:
                print(', ' + str(cards), end='')
            print('  sum: ' + str(Player))
        if show == False:
            print('Dealer\'s Hand: \tcovered, ' + str(dcard2))
            print('Your Hand: \t' + str(pcard1) + ', ' + str(pcard2) , end='')
            for cards in PlayerHand:
                print(', ' + str(cards), end='')
            print('\t\tsum: ' + str(Player))

    # Check dealers hand for 21 before hitting
    # If the dealer has >= 17 with first two cards it must stand. If it is 16 or under it must take a card.
    # It must then continue to take cards until the total is 17 or higher, but not over 21, or goes bust if it
    # is over 21. The dealer must count an ace as 11 and stand
    # Allow Aces to be 1 or 11
    # Add support for splitting and doubling down
    
    # Initializes and prepares the deck
    D = Deck()
    D.genDeck()
    D.shuffle()

    
    Player = 0              # Current value of Player hand
    Dealer = 0              # Current value of Dealer hand
    PlayerHand = []         # Successive cards added to Player after initial two

    # Two cards each are drawn for the player and dealer
    pcard1 = D.draw().value
    dcard1 = D.draw().value
    pcard2 = D.draw().value
    dcard2 = D.draw().value

    # The drawn cards are summed for the player and dealer
    Player = pcard1 + pcard2
    Dealer = dcard1 + dcard2

    # Prints known information about Player and Dealer hands
    printHands(False)

    print('would you like to stand (s), or hit(h)?')
    action = input()
    while action != 's' and action != 'h':
        print('invalid response, would you like to stand (s), or hit(h)?')
        action = input()
    if action == 's':
        print('Todo') # TODO
    if action == 'h':
        print('Todo') # TODO

        
    
print('Welcome to Blackjack!')
Blackjack()

