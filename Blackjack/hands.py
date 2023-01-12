'''
A hands class use to determine the value of the players and dealers hand
'''
from deck import Deck
from card import Card

class Hand:
    def __init__(self):
        '''
        Initialization of the hand class
        '''
        self.hand = []
        self.value = 0

    def addCard(self, card):
        '''
        Adds a card to the hand 
        '''
        self.hand.append(card)
        
    def checkHandValue(self):
        '''
        Calculates the players hand in blackjack
        '''
        nonNumCards = ['J', 'Q', 'K']
        dicOfValues = {}
        
        #Gets the card values of cards with numbers and stores it in a dictionary
        for i in range(2,11):
            dicOfValues[str(i)] = i
        
        #Gets the cards values of all non number cards but the A
        for i in nonNumCards:
            dicOfValues[i] = 10
        
        #Calculates the value of the hand
        total = 0
        aceSubtracted = False
        aceCount = 0
        for card in self.hand:
            #Get all non ace values
            if card.getCardValue() != 'A':
                total += dicOfValues[card.getCardValue()]

                #Extraneous case: Checks if hand value is 21, aceCount > 1, reduce the first ace to a value of 1
                if total > 21 and aceCount > 1 and aceSubtracted == False:
                    aceSubtracted = True
                    total -= 10
            else:
            #Calculate total with ace case
                aceCount += 1
                if total < 11:
                    total += 11
                else:
                    total += 1

                if total > 21 and aceCount > 1 and aceSubtracted == False:
                    total -= 10
                    aceSubtracted = True
                
                        
        
        return total
    
    def checkHandValueHouse(self):
        '''
        Displays only one of the house's card values
        '''
        nonNumCards = ['J', 'Q', 'K', 'A'] 
        dicOfValues = {}
        
        #Gets the card values of cards with numbers and stores it in a dictionary
        for i in range(2,11):
            dicOfValues[str(i)] = i
        
        #Gets the cards values of all non number cards 
        for i in nonNumCards:
            if i != 'A':
                dicOfValues[i] = 10
            else:
                dicOfValues[i] = 11

        total = 0
        total += dicOfValues[self.hand[1].getCardValue()]

        return total

    def displayHand(self):
        ''' 
        display the current players hand onto a single row
        '''
        #Inserts the visuals of the all the cards into a single list
        handVisual = []
        for card in self.hand:
            for visual in card.cardVisual():
                handVisual.append(visual)
        
        #Displays all the visual in a row
        for i in range(int(len(handVisual) / len(self.hand))):
            print(" ".join(handVisual[i::6]))

    def displayHouseHand(self):
        '''
        Displays one of the house's card and the other one is a hiidden card
        '''
        handVisual = []
        for i in range(len(self.hand)):
            if i == 0:
                for visual in self.hand[i].cardHiddenVisual():
                    handVisual.append(visual)
            else:
                for visual in self.hand[i].cardVisual():
                    handVisual.append(visual)

        for i in range(int(len(handVisual) / len(self.hand))):
            print(" ".join(handVisual[i::6]))
    



#Test
'''
hand = Hand()
deck = Deck()
deck.generate()
deck.shuffleDeck()


hand.addCard(deck.removeTop())
hand.addCard(deck.removeTop())


#print(hand.checkHandValue())
print("Displaying hand")
hand.displayHouseHand()
print(hand.checkHandValueHouse())
'''