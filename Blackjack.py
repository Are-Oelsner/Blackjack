# Author: Are Oelsner
# This is a single-deck blackjack simulation
import random
import time

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

            print('\nDealer\'s Hand: \t', end='')
            for cards in DealerHand:
                print(str(cards) +  ', ', end='')
            print(' ')
            print('Dealer sum: ' + str(Dealer))
            print('\nYour Hand: \t', end='')
            for cards in PlayerHand:
                print(str(cards) +  ', ', end='')
            print(' ')
            print('  sum: ' + str(Player))
        if show == False:
            print('Dealer\'s Hand: \tcovered, ' + str(dcard2))
            print('Your Hand: \t', end='')
            for cards in PlayerHand:
                print(str(cards) +  ', ', end='')
            print(' ')
            print('  sum: ' + str(Player))


    # Check dealers hand for 21 before hitting
    # If the dealer has >= 17 with first two cards it must stand. If it is 16 or under it must take a card.
    # It must then continue to take cards until the total is 17 or higher, but not over 21, or goes bust if it
    # is over 21. The dealer must count an ace as 11 and stand
    # Allow Aces to be 1 or 11
    # Add support for splitting and doubling down
    
    print('Game start!')
    # Initializes and prepares the deck
    D = Deck()
    D.genDeck()
    print('Shuffling the deck', end='')
    D.shuffle()
    time.sleep(.5)
    print('.', end='')
    time.sleep(.5)
    print('.', end='')
    time.sleep(.5)
    print('.\n\n')
    

    
    Player = 0              # Current value of Player hand
    Dealer = 0              # Current value of Dealer hand
    PlayerHand = []         # Successive cards added to Player after initial two
    DealerHand = []         # Successive cards added to Dealer after initial two

    # Two cards each are drawn for the player and dealer
    pcard1 = D.draw().value
    dcard1 = D.draw().value
    pcard2 = D.draw().value
    dcard2 = D.draw().value
    PlayerHand.append(pcard1)
    PlayerHand.append(pcard2)
    DealerHand.append(dcard1)
    DealerHand.append(dcard2)

    # The drawn cards are summed for the player and dealer
    Player = pcard1 + pcard2
    Dealer = dcard1 + dcard2

    # Prints known information about Player and Dealer hands
    printHands(False)

    if Player > 21:
        print('You went bust! Your hand had a value of ' + Player) # TODO add support for continued games
        
    print('\n')
    print('would you like to stand (s), or hit(h)?')
    action = input()
    while action != 's' and action != 'h':
        print('invalid response, would you like to stand (s), or hit(h)?')
        action = input()
    print('\n\n')
    if action == 'h':
        while action == 'h':
            newCard = D.draw()
            PlayerHand.append(newCard.value)
            Player += newCard.value
            print('You drew the ' + str(newCard.value) + ' of ' + newCard.suit)
            print('Your new total is ' + str(Player))
            if Player > 21:
                print('You went bust!')
                break
            print('would you like to stand (s), or hit(h)?')
            action = input()
            while action != 's' and action != 'h':
                print('invalid response, would you like to stand (s), or hit(h)?')
                action = input()
        
    if action == 's':
        while Dealer <= 16:
            newCard = D.draw()
            DealerHand.append(newCard.value)
            Dealer += newCard.value
            print('The Dealer drew a ' + str(newCard.value) + ' of ' + newCard.suit + '. Dealer total: ' + str(Dealer))
        if Dealer > 21 and Player <= 21:
            printHands(True)
            print('The dealer went bust with a total of ' + str(Dealer) + '! You win!')
            return True
        if Player > Dealer and Player <= 21: # TODO Add support for 21 getting double winnings
            printHands(True)
            print('You won!')
            return True
        if Player == Dealer and Player <= 21: 
            printHands(True)
            print('You tied!')
            return False
        if Dealer > Player and Dealer <= 21:
            printHands(True)
            print('You lost!')
            return False


        
    
numWins = 0
print('\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Blackjack!\n')
action = 'y'
while action == 'y':
    if Blackjack() == True:
        numWins += 1

    print('Thank you for playing! You have won ' + str(numWins) + ' games, would you like to play again? (y/n): ', end='')
    action = input()
    while action != 'y' and action != 'n':
        print('invalid response, would you like to play again? (y/n)')
        action = input()
print('\n\n\n\n\n\nThank you for playing! You won ' + str(numWins) + ' games!')



