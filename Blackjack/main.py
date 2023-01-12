'''
BlackJack Simulator - A python program use to simulate a game of blackjack
'''

from deck import Deck
from card import Card
from hands import Hand
from os import system, name
def clear_screen():
    '''
    Clears the screen on the window system
    '''
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def homeScreen():
    '''
    Prompts the user for a name and give the players 
    '''
    #Clear Screen
    clear_screen()
    #Prompts users to select a choice
    userChoice = input("Hello and welcome to the blackjack game simulator!\nPlease select what you would like to do \n1.Play Game \n2.Exit\n")
    if userChoice == "1":
        #Execute playGame function
        playGame()
    elif userChoice == "2":
        #Exit
        exit()
    else:
        exit()
    

def exit():
    """
    Displays a farewell message
    """
    print("Thanks for playing and see you next time!")

def playGame():
    '''
    Executes the blackjack game
    '''
    clear_screen()
    #Global Variables
    exit = False
    balance = 1000
    print("Welcome to the BlackJack table!")

    #Loop the game until the player chooses to leave or goes bankedrupt
    while not exit:
        clear_screen()
        displayBalance(balance)

        #Prompt the user how much he wants to wager
        wagerAmount = input("How much money do you want to wager?\n")
        print("")

        #Check if the wagerAmount is an integer and is valid amount
        while wagerAmount.isdigit() == False or int(wagerAmount) > balance or int(wagerAmount) <= 0:
            wagerAmount = input("Invalid wager, please reenter how much money do you want to wager\n")
            print("")
        wagerAmount = int(wagerAmount)

        #Create playerHand and houseHand and deck
        playerHand = Hand()
        houseHand = Hand()
        deckOfCard = Deck()
        deckOfCard.clearDeck()
        deckOfCard.generate()
        deckOfCard.shuffleDeck()

        #Deal cards to each players from deck
        for i in range(2):
            playerHand.addCard(deckOfCard.removeTop())
            houseHand.addCard(deckOfCard.removeTop())

        #Calculate total value of each players hands
        displayPlayerHand(playerHand)
        displayHouseHandHidden(houseHand)

        #Check if Player Has blackjack
        blackjack = False 
        if playerHand.checkHandValue() == 21:
            blackjack = True

        #Prompt user if he wants to hit or stand
        #Loop til player stops hitting or player busts or player has blackjack
        
        stand = False
        playerBusted = False
        while not stand and not playerBusted and not blackjack:
            choice = input("Would you like to hit(h) or stand(s)? Press h to hit and press s to stand\n")
            if choice == 'h' or choice == 'H':
                playerHand.addCard(deckOfCard.removeTop())
                if playerHand.checkHandValue() > 21:
                    print(f"Player has busted and lost ${str(wagerAmount)}!")
                    playerBusted = True
                elif playerHand.checkHandValue() == 21:
                    print(f"Player hit 21, automatically stand!")
                    stand = True
            elif choice == 's' or choice == 'S':
                stand = True
            
            
            displayPlayerHand(playerHand)
            displayHouseHandHidden(houseHand)
            print("")

        #Reveal house's cards
        if playerBusted == False and blackjack == False:
            print("Revealing House's Cards")
            displayPlayerHand(playerHand)
            displayHouseHand(houseHand)
            print("")

        #House Hits until hand is greater than 16
        houseBusted = False
        while houseHand.checkHandValue() <= 16 and not playerBusted and not blackjack:
            input("Press enter to watch house hit")
            houseHand.addCard(deckOfCard.removeTop())
            displayPlayerHand(playerHand)
            displayHouseHand(houseHand)
            print("")

        if houseHand.checkHandValue() > 21:
            houseBusted = True

        #Determine winner
        if blackjack == True:
            print("Black Jack!")
            wagerAmount = wagerAmount * 2
            print(f"Player wins ${str(wagerAmount)}!")
            balance += wagerAmount

        elif playerBusted == True:
            print(f"Player loses ${str(wagerAmount)}!")
            balance -= wagerAmount

        elif houseBusted == True:
            print(f"Player Wins ${str(wagerAmount)}!")
            balance += wagerAmount

        elif playerHand.checkHandValue() < houseHand.checkHandValue():
            print(f"Player loses ${str(wagerAmount)}!")
            balance -= wagerAmount

        elif playerHand.checkHandValue() > houseHand.checkHandValue():
            print(f"Player wins ${str(wagerAmount)}!")
            balance += wagerAmount
            
        else:
            print(f"Player and House Draws ${str(wagerAmount)}!")

        #Check if player went bankrupt
        displayBalance(balance)
        if balance == 0:
            print("Player went bankrupt!")
            print(f"You cashed out {str(balance)}!")
            exit = True
            input("Press Enter to exit back to Home Screen")
            print("")

        #Check if player still has money in their balance
        #Prompt user if they want to keep on playing the game
        if balance > 0:
            playAgain = input("Would you like to play again? Press (y) for yes or (n) for no\n")
            if playAgain == "y" or playAgain == "Y":
                exit = False
            elif playAgain == "n" or playAgain == "N":
                print(f"You cashed out ${str(balance)}!")
                exit = True
                input("Press Enter to exit back to homescreen!")

    homeScreen()

def displayBalance(balance):
    '''
    Displays the players current balance and the value of their hands
    '''
    print(f"Your current balance is ${balance}")

def displayPlayerHand(hand):
    '''
    Displays the players hand and the value of their hands
    '''
    print("Player's Hand Value: " + str(hand.checkHandValue()))
    hand.displayHand()
    
def displayHouseHand(hand):
    '''
    Displays the houses hand without hidden value
    '''
    print("House's Hand Value: " + str(hand.checkHandValue()))
    hand.displayHand()
    
def displayHouseHandHidden(hand):
    '''
    Displays the houses hand with hidden value
    '''
    print("House's Hand Value: " + str(hand.checkHandValueHouse()))
    hand.displayHouseHand()


    
def main():
    #Displays the homescreen and prompts user for an option
    homeScreen()


main()


