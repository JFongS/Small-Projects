'''
Deck class for the following blackjack game
'''
from card import Card
import random
class Deck:
    def __init__(self):
        '''
        Initializes the deck class
        '''
        self.deck = []
        self.suits = ["♠", "♥", "♦" , "♣"]
        self.cardVal = ['A','2','3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def shuffleDeck(self):
        '''
        Shuffles the deck in a random order
        '''
        random.shuffle(self.deck)

    def generate(self):
        '''
        Adds 52 cards into the deck with all the possible cardVal and suit combination
        '''
        for x in range(len(self.cardVal)): 
            for y in range(len(self.suits)):
                self.deck.append(Card(self.cardVal[x],self.suits[y]))

    def removeTop(self):
        '''
        Removes the card from the top of the deck
        '''
        return self.deck.pop()
    
    def clearDeck(self):
        '''
        Remove all the cards from deck so we can regenerate a new deck
        '''
        self.deck = []

    def displayDeck(self):
        '''
        Testing if the Deck diplays all the cards inside the deck
        '''

        for i in self.deck:
           for y in i.cardVisual():
                print(y)

#Test
'''
deck1 = Deck()
deck1.generate()
deck1.shuffleDeck()
deck1.displayDeck()
'''