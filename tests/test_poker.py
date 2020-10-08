from poker.player import Player
from poker.poker import Hand
from poker.table import Table


def init_hand():
    n_players = 5
    table = Table(n_players)
    player1, player2, player3, player4, player5 = (Player(500) for _ in range(n_players))
    player1.sit(table, 100)
    player2.sit(table, 100)
    player3.sit(table, 100)
    player4.sit(table, 100)
    player5.sit(table, 100)

    hand = Hand(table)
    return hand


def test_deal():
    hand = init_hand()
    hand.deal_hole()
    assert len(hand._table.seats[0].player.hole.cards) == 2
    assert hand._table.seats[4].player.hole.is_suited in [True, False]
    assert len(hand._table.seats[3].player.hole.suits) == 2


def test_community():
    hand = init_hand()
    hand.init_hand()
    hand.deal_hole()
    hand.open_flop()
    assert len(hand._table.seats[1].player.community_cards.cards) == 3
    hand.open_turn_or_river()
    assert len(hand._table.seats[2].player.community_cards.cards) == 4
    hand.open_turn_or_river()
    assert hand._table.seats[3].player.community_cards.cards == hand._table.seats[4].player.community_cards.cards
