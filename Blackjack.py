# Author: Are Oelsner
# This is a single-deck blackjack simulation
    # If the dealer has >= 17 with first two cards it must stand. If it is 16 or under it must take a card.
    # It must then continue to take cards until the total is 17 or higher, but not over 21, or goes bust if it
    # is over 21. The dealer must count an ace as 11 and stand
    # Allow Aces to be 1 or 11
    # Add support for splitting and doubling down
    #The dealer must count an ace as 11 and stand
    #Allow Aces to be 1 or 11
    #Add support for splitting and doubling down
    #Check dealers hand for 21 before hitting

    
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
def Blackjack(wallet):
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
            print('Player wallet: ' + str(wallet) + ', Player bet: ' + str(bet))
            print('Player sum: ' + str(Player))
        if show == False:
            print('Dealer\'s Hand: \tcovered, ' + str(dcard2))
            print('Your Hand: \t', end='')
            for cards in PlayerHand:
                print(str(cards) +  ', ', end='')
            print(' ')
            print('Player wallet: ' + str(wallet) + ', Player bet: ' + str(bet))
            print('Player sum: ' + str(Player))


    print('Game start!')
    # Initializes and prepares the deck
    D = Deck()
    D.genDeck()
    D.shuffle()

    print('Shuffling the deck')

    time.sleep(.5)

    print('...', end='')

    time.sleep(.5)

    print('.\n\n')

    print('You have ' + str(wallet) + ' dollars, how much would you like to bet?  ', end='')
    bet = 0
    while bet <= 0 or bet > wallet:
        print('Invalid input: ' + str(bet) + ', please enter a number between 1 and ' + str(wallet))
        bet = int(input())
    wallet -= bet

    
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
        print('You went bust! You lost $' + str(bet) + '!')
        return (False, wallet)
        
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
                return (False, wallet)
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
        if Dealer < 21 and Player == 21:
            printHands(True)
            print('Blackjack! You won $' + str(bet * 1.5) + '!')
            return(True, wallet + (bet * 1.5))
        if Dealer > 21 and Player <= 21:
            printHands(True)
            print('The dealer went bust with a total of ' + str(Dealer) + '! You won $' + str(bet) + '!')
            return (True, wallet + (2 * bet))
        if Player > Dealer and Player <= 21: 
            printHands(True)
            print('You won $' + str(bet) + '!')
            return (True, wallet + (2 * bet))
        if Player == Dealer and Player <= 21: 
            printHands(True)
            print('You tied!')
            return (False, wallet + bet)
        if Dealer > Player and Dealer <= 21:
            printHands(True)
            print('You lost $' + str(bet) + '!')
            return (False, wallet)


        
    
# Game Start
numWins = 0     # numWins tracks number of wins in current session
wallet = 1000   # wallet tracks the current player balance that bets are drawn from


# Introductory Banner
print(' __          __  _                            _          ____  _            _    _            _    _ ')
print(' \ \        / / | |                          | |        |  _ \| |          | |  (_)          | |  | |')
print('  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_) | | __ _  ___| | ___  __ _  ___| | _| |')
print('   \ \/  \/ / _ \ |/ __/ _ \| \'_ ` _ \ / _ \ | __/ _ \  |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ / |')
print('    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_) | | (_| | (__|   <| | (_| | (__|   <|_| ')
print('     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_(_) ')
print('                                                                               _/ |                ')
print('     Game by Are Oelsner                                                      |__/                \n')



# Game loop
action = 'y'
while action == 'y' and wallet > 0:
    game = Blackjack(wallet)
    wallet = game[1]
    if game[0] == True:
        numWins += 1

    if wallet > 0:
        print('Thank you for playing! You have won ' + str(numWins) + ' games and have $' + str(wallet) + ', would you like to play again? (y/n): ', end='')
        action = input()
        while action != 'y' and action != 'n':
            print('invalid response, would you like to play again? (y/n)')
            action = input()
    if wallet <= 0:
        print('You ran out of money!')
print('\n\n\n\n\nThank you for playing! You won ' + str(numWins) + ' games and have $' + str(wallet) + '!')



