from carddeck import CardDeck

cd1 = CardDeck("Delilah")
print(cd1)

cd1.shuffle()
card = cd1.deal()
print(card)

cd2 = CardDeck("Balthazar")

print("function:", cd1.get_dealer())
# print(CardDeck.get_dealer(cd1))

print("property:", cd1.dealer)

cd1.dealer = "Ferdinand"
print(cd1.dealer)

print(CardDeck.SUITS)
print(cd1.SUITS)
cd1.shuffle()
print(cd1.cards)

for i in range(10):
    print(cd1.deal())
print()

print(len(cd1.cards))
