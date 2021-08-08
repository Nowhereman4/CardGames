from Game import Game
from time import sleep
#war is played with two players
warGame = Game(2)
warGame.dealDeck()
x=0
while(x != 20):
    warGame.players[0].hand.removeFromBeginning()
    warGame.players[1].hand.removeFromBeginning()
    x+=1
while(warGame.players[0].hand.head != None and warGame.players[1].hand.head != None):
    sleep(.5)
    cardOne = warGame.players[0].hand.removeFromBeginning()
    cardTwo = warGame.players[1].hand.removeFromBeginning()
    # if P1 has the higher card, put both cards back in P1s deck
    # if they are equal,
    if(cardOne.getRank() > cardTwo.getRank()):
        warGame.players[0].hand.insertAtEnd(cardOne)
        warGame.players[0].hand.insertAtEnd(cardTwo)
        print("player one has", cardOne.__str__(), "and player two has", cardTwo.__str__(), "and player one won")
    # if the cards have the same value. draw three cards (W A R spells war) and the fourth is the one compared
    elif(cardOne.getRank() == cardTwo.getRank()):
        warGame.players[0].hand.removeFromBeginning()
        warGame.players[1].hand.removeFromBeginning()
        warGame.players[0].hand.removeFromBeginning()
        warGame.players[1].hand.removeFromBeginning()
        warGame.players[0].hand.removeFromBeginning()
        warGame.players[1].hand.removeFromBeginning()
        print("we have a tie")

    else:
        # player two won
        print("player two has the higher card")
        warGame.players[1].hand.insertAtEnd(cardOne)
        warGame.players[1].hand.insertAtEnd(cardTwo)




if(warGame.players[0].hand.head == None):
    name = warGame.players[1].getName()
    warGame.players[1].printHand()
else:
    name = warGame.players[0].getName()
    warGame.players[0].printHand()

print("player",name,"won!")