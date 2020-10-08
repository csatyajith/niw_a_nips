from poker.poker import CommunityCards


class Hole:
    def __init__(self,):
        self.cards = []
        self.values = []
        self.suits = []
        self.is_suited = None

    def add(self, card):
        self.cards.append(card)
        self.values.append(card.value)
        self.suits.append(card.suit)
        self.is_suited = True if self.suits.count(self.suits[0]) == len(self.suits) else False


class Player:
    def __init__(self, cash_balance):
        self.cash_balance = cash_balance
        self.table = None
        self.betting_stack = None
        self.seat = None
        self.hole = Hole()
        self.community_cards = CommunityCards()

    def sit(self, table, buy_in_amount):
        self.seat = table.player_sit(self, buy_in_amount)
        self.betting_stack = buy_in_amount
        self.table = table
        self.cash_balance = self.cash_balance - buy_in_amount

    def stand(self):
        self.table.player_stand(self)
        self.table = None
        self.betting_stack = None
        self.cash_balance = self.cash_balance + self.betting_stack

    def start_hand(self, community_cards):
        self.community_cards = community_cards

    def get_dealt(self, hole_card):
        self.hole.add(hole_card)

    def end_hand(self):
        self.hole = Hole()

