# this driver is used  to test various functionalities of both card and deck to make sure they work as intended

from Deck import Deck
from Card import Card

# creating a new deck with the head being a random card
a = Deck()
a.head = Card("a", 0, 0, "fnjk3i", False)

# create three new cards (b, c, d and set C next to D and b next to D; b-> c-> d
b = Card("a", 0, 0, "aaa", False)
b.setName("card b")
c = Card("a", 0, 0, "aaa", False)
c.setName("card c")
d = Card("dd", 0,0,"efed", False)
c.setNext(d)
print(b.getName())
b.setNext(c)

# insert b to the "top" of the deck ,which in turn adds c and d
a.insertAtBeginning(b)

# remove the "top" card
ggg = a.removeFromBeginning()
print(ggg.getName())

realDeck = Deck()
realDeck.buildDeck()

realDeck.printAll()
print("aaaa\n\n")
thirdCard = realDeck.getNumberedCard(3)
realDeck.printAll()
print(thirdCard.__str__())