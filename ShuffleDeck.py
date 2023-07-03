import random
import itertools

cardsSymbol = ["Spade", "Diamond", "Hearts", "Club"]

deck = list(itertools.product(range(1,14), cardsSymbol))

random.shuffle(deck)

print("deck => ", deck)

print("From above list top five cards will be : ")

for i in range(5) :
    print("Card", (i+1), " =", deck[i][0], "of", deck[i][1])
