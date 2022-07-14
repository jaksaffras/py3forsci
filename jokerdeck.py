from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call in parent...
        joker1 = ("\U0001F0CF", 'JOKER')
        joker2 = ("\U0001F0DF", 'JOKER')
        self._cards.append(joker1)
        self._cards.append(joker2)



