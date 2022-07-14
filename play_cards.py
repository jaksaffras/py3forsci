from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Beatrice")
d2 = CardDeck("Lakshmi")

print(d1, type(d1))
print(d2, type(d2))

print(d1.dealer, d2.dealer)

d1.dealer = "Hercule"

# d2.dealer = 48.7
d2.dealer = "Hortense"

print(d1.dealer, d2.dealer)

d1.shuffle()
print(d1.cards, '\n')

for _ in range(5):
    print(d1.draw())
print()
print('-' * 60)

j1 = JokerDeck("Jimmy")
j1.shuffle()
print(j1.cards, '\n')

for _ in range(10):
    print(j1.draw())
print()

print(len(d1), len(d2), len(j1))

x = d1 + j1
print(x)
print(x.cards)
print(len(x))
