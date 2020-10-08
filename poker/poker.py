import pydealer


class CommunityCards:
    def __init__(self):
        self.cards = []

    def add(self, cards):
        for card in cards:
            self.cards.append(card)


class Hand:
    def __init__(self, table):
        self._table = table
        self._deck = pydealer.Deck()
        self.community_cards = CommunityCards()
        self.init_hand()

    def init_hand(self):
        self._deck = pydealer.Deck()
        self._deck.shuffle()
        for seat in self._table.seats:
            if seat.occupied is True:
                seat.player.start_hand(self.community_cards)

    def deal_hole(self):
        for _ in range(2):
            for seat in self._table.seats:
                if seat.occupied is True:
                    seat.player.get_dealt(self._deck.deal()[0])

    def open_flop(self):
        self._deck.deal()
        self.community_cards.add(self._deck.deal(3))

    def open_turn_or_river(self):
        self._deck.deal()
        self.community_cards.add(self._deck.deal())
