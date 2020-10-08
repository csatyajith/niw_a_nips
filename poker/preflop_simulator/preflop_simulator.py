from collections import Counter

from pydealer import Deck, Stack, Card

from poker.hand_strength import HandStrength


class HandSimulator:

    def __init__(self):
        self.deck = Deck()
        self.hand_strength = HandStrength()

    def simulate(self, hero_cards, n_simulations, n_villains=3, villain_cards=None):
        self.deck.shuffle()
        hero_card_names = [hero_cards[0].name, hero_cards[1].name]

        win_counter = Counter()
        for _ in range(n_simulations):
            self.deck = Deck()
            self.deck.shuffle()
            self.deck.get_list(hero_card_names)
            all_hands = {i + 1: self.deck.deal(2) for i in range(n_villains)}
            all_hands[0] = Stack(cards=[hero_cards[0], hero_cards[1]])
            community_cards = self.deck.deal(5)
            for h in all_hands:
                all_hands[h].add(community_cards)
            winners = self.hand_strength.compare_hands(all_hands)
            for w in winners:
                win_counter[w] += 1
        print(win_counter)


if __name__ == '__main__':
    hs = HandSimulator()
    hc = [Card('Ace', 'Spades'), Card('Ace', 'Clubs')]
    hs.simulate(hc, 100)
