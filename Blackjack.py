# This is a multi-deck blackjack gambling simulation created by Are Oelsner
# money = 100
import random
class Deck:
    def __init__(self):
        self.deck = []
    
    def genDeck(self):
        for suit in ('hearts', 'spades', 'clubs', 'diamonds'):
            for value in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10):
                self.deck.append(Card(value, suit))

    def printDeck(self):
        for cards in self.deck:
            cards.print()
        print(len(self.deck))

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Draws and returns the top card of the deck, removing it from the deck
    def draw(self):
        return self.deck.pop()

    
            
    
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def generate(self):
        self.value = random.randint(1, 13)
        self.suit = random.randint(1,4)
    def print(self):
        print('suit: ' + str(self.suit) + ', value: ' + str(self.value))
    def getValue(self):
        return self.value

def Blackjack():
    def printHands(show):
        if show:
            print('Dealer\'s Hand: ' + str(dcard1) + ', ' + str(dcard2) + ', ' + str(dcard3) +'  sum: ' + str((dcard1 + dcard2 + dcard3)))
            print('Your Hand: ' + str(pcard1) + ', ' + str(pcard2) , end='')
            for cards in PlayerHand:
                print(', ' + str(cards), end='')
            print('  sum: ' + str(Player))
        if !show:
            print('Dealer\'s Hand: covered, ' + str(dcard2))
            print('Your Hand: ' + pcard1 + ', ' + pcard2 , end='')
            for cards in PlayerHand:
                print(', ' + str(cards), end='')
            print('  sum: ' + Player)
    # check dealers hand for 21 before hitting
    D = Deck()
    D.genDeck()
    D.shuffle()
    Player = 0
    Dealer = 0
    pcard1 = D.draw().value
    pcard2 = D.draw().value
    dcard1 = D.draw().value
    dcard2 = D.draw().value

    
    print(D.draw().getValue())
    Player = D.draw().value
    Player += D.draw().value
    print(Player)

    D.draw().print()
    D.printDeck()
    

Blackjack()

