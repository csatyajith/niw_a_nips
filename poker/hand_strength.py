from collections import Counter
from enum import Enum

from pydealer import Stack
from pydealer.const import POKER_RANKS


class InvalidHandException(BaseException):
    pass


class HandNames(Enum):
    HIGH_CARD = "high_card"
    PAIR = "pair"
    TWO_PAIR = "two_pair"
    TRIPS = "trips"
    STRAIGHT = "straight"
    FLUSH = "flush"
    FULL_HOUSE = "full_house"
    QUADS = "quads"
    STRAIGHT_FLUSH = "straight_flush"


class HandStrength:
    def __init__(self):
        self.sequence = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.ranks = POKER_RANKS["values"]

    @staticmethod
    def sort_descending(cards: Stack):
        cards.sort()
        cards.reverse()
        return cards

    @staticmethod
    def seq_in_seq(sub, full):
        f = ''.join([repr(d) for d in full]).replace("'", "")
        s = ''.join([repr(d) for d in sub]).replace("'", "")
        return s in f

    def is_straight_flush(self, sorted_cards):
        splits = {s: Stack() for s in self.suits}
        for i, card in enumerate(sorted_cards):
            splits[card.suit].add(card)
        for suit in splits:
            if len(splits[suit]) >= 5:
                sorted_flush = self.sort_descending(splits[suit])
                is_straight, straight_cards = self.is_straight(sorted_flush)
                return is_straight, straight_cards
        return False, None

    def is_quads(self, sorted_cards: Stack):
        best_five = Stack()
        freq_counter = Counter()
        for card in sorted_cards:
            freq_counter[card.value] += 1
        most_freq_card = freq_counter.most_common()[0]
        if most_freq_card[1] < 4:
            return False, None
        for card in sorted_cards:
            if card.value == most_freq_card[0]:
                best_five.add(card)
        for card in sorted_cards:
            if card.value != most_freq_card[0]:
                best_five.add(card)
        return True, best_five[0:5]

    def is_full_house(self, sorted_cards):
        best_five = Stack()
        freq_counter = Counter()

        for card in sorted_cards:
            freq_counter[card.value] += 1
        most_freq_card = freq_counter.most_common()[0]
        second_most_freq_card = freq_counter.most_common()[1]
        if most_freq_card[1] < 3 or second_most_freq_card[1] < 2:
            return False, None

        if most_freq_card[1] == second_most_freq_card[1] and \
                self.ranks[most_freq_card[0]] < self.ranks[second_most_freq_card[0]]:
            boat_1, boat_2 = second_most_freq_card[0], most_freq_card[0]
        else:
            boat_1, boat_2 = most_freq_card[0], second_most_freq_card[0]

        for card in sorted_cards:
            if card.value == boat_1:
                best_five.add(card)
        for card in sorted_cards:
            if card.value == boat_2:
                best_five.add(card)
        return True, best_five[0:5]

    def is_flush(self, sorted_cards):
        splits = {s: Stack() for s in self.suits}
        for i, card in enumerate(sorted_cards):
            splits[card.suit].add(card)
        for suit in splits:
            if len(splits[suit]) >= 5:
                sorted_flush = self.sort_descending(splits[suit])
                return True, sorted_flush[0:5]
        return False, None

    def is_straight(self, sorted_cards):
        values = list({card.value: None for card in sorted_cards}.keys())
        value_order = []
        if "Ace" in values and self.seq_in_seq(['5', '4', '3', '2'], values):
            value_order = ['5', '4', '3', '2', 'Ace']
        else:
            for i in range(len(values) - 4):
                if self.seq_in_seq(values[i:i + 5], self.sequence):
                    value_order = values[i:i + 5]
                    break
        if len(value_order) == 0:
            return False, None
        best_five = [None for _ in range(5)]
        for card in sorted_cards:
            if card.value in value_order:
                best_five[value_order.index(card.value)] = card
        return True, best_five

    def is_trips(self, sorted_cards: Stack):
        best_five = Stack()
        freq_counter = Counter()
        for card in sorted_cards:
            freq_counter[card.value] += 1
        most_freq_card = freq_counter.most_common()[0]
        if most_freq_card[1] < 3:
            return False, None
        for card in sorted_cards:
            if card.value == most_freq_card[0]:
                best_five.add(card)
        for card in sorted_cards:
            if card.value != most_freq_card[0]:
                best_five.add(card)
        return True, best_five[0:5]

    def is_two_pair(self, sorted_cards):
        best_five = Stack()
        freq_counter = Counter()

        for card in sorted_cards:
            freq_counter[card.value] += 1
        most_freq_card = freq_counter.most_common()[0]
        second_most_freq_card = freq_counter.most_common()[1]
        third_most_freq_card = freq_counter.most_common()[2]
        if most_freq_card[1] < 2 or second_most_freq_card[1] < 2:
            return False, None

        if most_freq_card[1] == second_most_freq_card[1] == third_most_freq_card[1]:
            freqs = {
                most_freq_card[0]: self.ranks[freq_counter.most_common()[0][0]],
                second_most_freq_card[0]: self.ranks[freq_counter.most_common()[1][0]],
                third_most_freq_card[0]: self.ranks[freq_counter.most_common()[2][0]]
            }
            sorted_freqs = sorted(freqs, key=lambda k: freqs[k])[::-1]
            tp1 = sorted_freqs[0]
            tp2 = sorted_freqs[1]
        else:
            tp1, tp2 = most_freq_card[0], second_most_freq_card[0]

        for card in sorted_cards:
            if card.value == tp1:
                best_five.add(card)
        for card in sorted_cards:
            if card.value == tp2:
                best_five.add(card)
        for card in sorted_cards:
            if card.value not in [tp1, tp2]:
                best_five.add(card)
        return True, best_five[0:5]

    def is_pair(self, sorted_cards):
        best_five = Stack()
        freq_counter = Counter()

        for card in sorted_cards:
            freq_counter[card.value] += 1
        most_freq_card = freq_counter.most_common()[0]
        if most_freq_card[1] < 2:
            return False, None
        for card in sorted_cards:
            if card.value == most_freq_card[0]:
                best_five.add(card)
        for card in sorted_cards:
            if card.value != most_freq_card[0]:
                best_five.add(card)
        return True, best_five[0:5]

    def is_high_card(self, sorted_cards):
        best_five = Stack()
        for card in sorted_cards:
            best_five.add(card)
        return True, best_five[0:5]

    def identify_hand(self, cards: Stack):
        sorted_cards = self.sort_descending(cards)
        is_straight_flush, best_five = self.is_straight_flush(sorted_cards)
        if is_straight_flush:
            return HandNames.STRAIGHT_FLUSH, best_five

        is_quads, best_five = self.is_quads(sorted_cards)
        if is_quads:
            return HandNames.QUADS, best_five

        is_full_house, best_five = self.is_full_house(sorted_cards)
        if is_full_house:
            return HandNames.FULL_HOUSE, best_five

        is_flush, best_five = self.is_flush(sorted_cards)
        if is_flush:
            return HandNames.FLUSH, best_five

        is_straight, best_five = self.is_straight(sorted_cards)
        if is_straight:
            return HandNames.STRAIGHT, best_five

        is_trips, best_five = self.is_trips(sorted_cards)
        if is_trips:
            return HandNames.TRIPS, best_five

        is_two_pair, best_five = self.is_two_pair(sorted_cards)
        if is_two_pair:
            return HandNames.TWO_PAIR, best_five

        is_pair, best_five = self.is_pair(sorted_cards)
        if is_pair:
            return HandNames.PAIR, best_five

        is_high_card, best_five = self.is_high_card(sorted_cards)
        if is_high_card:
            return HandNames.HIGH_CARD, best_five

        raise InvalidHandException

    def compare_hands(self, hands):
        order = [HandNames.STRAIGHT_FLUSH,
                 HandNames.QUADS,
                 HandNames.FULL_HOUSE,
                 HandNames.FLUSH,
                 HandNames.STRAIGHT,
                 HandNames.TRIPS,
                 HandNames.TWO_PAIR,
                 HandNames.PAIR,
                 HandNames.HIGH_CARD]
        values = {h_n: [] for h_n in order}
        winners = []
        best_fives = {}
        for i in hands.keys():
            hand_name, best_five = self.identify_hand(hands[i])
            values[hand_name].append(i)
            best_fives[i] = best_five
        for h_n in values:
            if len(values[h_n]) == 0:
                continue
            elif len(values[h_n]) > 1:
                loser_list = []
                for i in range(5):
                    max_val = self.ranks[
                        best_fives[max(values[h_n], key=lambda k: self.ranks[best_fives[k][i].value])][i].value]
                    for p in values[h_n]:
                        if self.ranks[best_fives[p][i].value] < max_val:
                            loser_list.append(p)
                    for l in loser_list:
                        values[h_n].remove(l)
                    if len(values[h_n]) == 1:
                        return values[h_n]
                return values[h_n]

            else:
                return values[h_n]
