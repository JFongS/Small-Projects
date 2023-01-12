'''
Card Class for black jack game
'''
class Card:
    def __init__(self, cardValue, suit):
        '''
        Initialize Cards
        Suit is the suit of the card
        CardValue is the value of the card
        '''
        self.cardValue = cardValue
        self.suit = suit

    def getCardValue(self):
        '''
        returns the cardValue
        '''
        return self.cardValue
        
    def cardVisual(self):
        '''
        Stores the visuals of the cards into a list, each index contains a component of the card like the top 
        of the card, the middle of the card, the bottom of the card, etc.
        '''
        if self.cardValue == 10 or self.cardValue == '10':
            visual = [
                "┌───────┐",
                f"|{str(self.cardValue)}     |",
                f"|   {self.suit}   |",
                "|       |",
                f"|     {str(self.cardValue)}|",
                "└───────┘"
            ]
        else:
            visual = [
                "┌───────┐",
                f"|{str(self.cardValue)}      |",
                f"|   {self.suit}   |",
                '|       |',
                f"|      {str(self.cardValue)}|",
                "└───────┘"
            ]
        return visual

    def cardHiddenVisual(self):
        '''
        Stores the hidden visuals of the cards into a list, each index contains a component of the card like the top 
        of the card, the middle of the card, the bottom of the card, etc.
        '''
        visual = [
                "┌───────┐",
                f"|?      |",
                f"|   {self.suit}   |",
                "|       |",
                f"|      ?|",
                "└───────┘"
            ]
        return visual 

    def displayCard(self):
        '''
        Displays the cards and the suit of the card
        '''
        print('┌───────┐')
        #Checks if the card value is 10 so we can format the card properly
        if self.cardValue == '10' or self.cardValue == 10:
            print(f"|{str(self.cardValue)}     |")
        else: print(f"|{str(self.cardValue)}      |")
        print('|       |')
        print(f"|   {self.suit}   |")
        print('|       |')
        #Checks if the card value is 10 so we can format the card properly
        if self.cardValue == '10' or self.cardValue == 10:
            print(f"|     {str(self.cardValue)}|")
        else:
            print(f"|      {str(self.cardValue)}|")
        print(f"└───────┘")

    def displayCardHidden(self):
        '''
        Displays the cards and the suit of the card
        '''
        print('┌───────┐')
        print(f"|?      |")
        print('|       |')
        print(f"|   ?   |")
        print('|       |')
        print(f"|      ?|")
        print(f"└───────┘")
        


#Testing 

card1 = Card("10", "♣")
'''
for i in range(len(card1.cardVisual())):
    print(card1.cardVisual()[i])

for i in range(len(card1.cardVisual())):
    print(card1.cardHiddenVisual()[i])
'''


