from pydealer import Card, Stack

from poker.hand_strength import HandStrength, HandNames


def init_hands():
    hands = HandStrength()
    return hands


def stack_and_sort(cards):
    player_hand = Stack(cards=cards)
    player_hand = HandStrength.sort_descending(player_hand)
    return player_hand


def test_is_straight_flush():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Spades"), Card("3", "Spades"), Card("4", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_straight_flush, straight_flush_cards = hands.is_straight_flush(player_hand)
    assert is_straight_flush
    assert straight_flush_cards[0].value == "5"
    assert straight_flush_cards[2].value == "3"
    assert straight_flush_cards[3].value == "2"
    assert straight_flush_cards[4].value == "Ace"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("King", "Spades"), Card("Queen", "Spades"), Card("Jack", "Spades"),
         Card("10", "Spades"), Card("8", "Diamonds"), Card("King", "Hearts")])
    is_straight_flush, straight_flush_cards = hands.is_straight_flush(player_hand)
    assert is_straight_flush
    assert straight_flush_cards[0].value == "Ace"
    assert straight_flush_cards[2].value == "Queen"
    assert straight_flush_cards[4].value == "10"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("3", "Hearts")])
    is_straight_flush, straight_flush_cards = hands.is_straight_flush(player_hand)
    assert not is_straight_flush

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("King", "Spades"), Card("Queen", "Spades"), Card("Jack", "Diamonds"),
         Card("10", "Spades"), Card("8", "Spades"), Card("King", "Hearts")])
    is_straight_flush, straight_flush_cards = hands.is_straight_flush(player_hand)
    assert not is_straight_flush


def test_is_quads():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("Ace", "Hearts"), Card("Ace", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_quads, quads_cards = hands.is_quads(player_hand)
    assert is_quads
    assert quads_cards[0].value == "Ace"
    assert quads_cards[3].value == "Ace"
    assert quads_cards[4].value == "King"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("Ace", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_quads, quads_cards = hands.is_quads(player_hand)
    assert not is_quads


def test_is_full_house():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Clubs"), Card("Ace", "Hearts"), Card("7", "Spades"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_full_house, full_house_cards = hands.is_full_house(player_hand)
    assert is_full_house
    assert full_house_cards[0].value == "Ace"
    assert full_house_cards[2].value == "Ace"
    assert full_house_cards[3].value == "King"
    assert full_house_cards[4].value == "King"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("3", "Hearts")])
    is_full_house, full_house_cards = hands.is_full_house(player_hand)
    assert not is_full_house


def test_flush():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Jack", "Spades"), Card("Ace", "Hearts"), Card("7", "Spades"),
         Card("King", "Spades"), Card("Queen", "Diamonds"), Card("2", "Spades")])
    is_flush, flush_cards = hands.is_flush(player_hand)
    assert is_flush
    assert flush_cards[0].value == "Ace"
    assert flush_cards[1].value == "King"
    assert flush_cards[2].value == "Jack"
    assert flush_cards[3].value == "7"
    assert flush_cards[4].value == "2"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("3", "Hearts")])
    is_flush, flush_cards = hands.is_flush(player_hand)
    assert not is_flush


def test_is_straight():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Clubs"), Card("3", "Hearts"), Card("4", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_straight, straight_cards = hands.is_straight(player_hand)
    assert is_straight
    assert straight_cards[0].value == "5"
    assert straight_cards[2].value == "3"
    assert straight_cards[3].value == "2"
    assert straight_cards[4].value == "Ace"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("King", "Clubs"), Card("Queen", "Hearts"), Card("Jack", "Spades"),
         Card("10", "Spades"), Card("8", "Diamonds"), Card("King", "Hearts")])
    is_straight, straight_cards = hands.is_straight(player_hand)
    assert is_straight
    assert straight_cards[0].value == "Ace"
    assert straight_cards[2].value == "Queen"
    assert straight_cards[4].value == "10"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("3", "Hearts")])
    is_straight, straight_cards = hands.is_straight(player_hand)
    assert not is_straight


def test_is_trips():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Jack", "Diamonds"), Card("Ace", "Hearts"), Card("Ace", "Clubs"),
         Card("King", "Spades"), Card("Queen", "Diamonds"), Card("2", "Hearts")])
    is_trips, trips_cards = hands.is_trips(player_hand)
    assert is_trips
    assert trips_cards[0].value == "Ace"
    assert trips_cards[2].value == "Ace"
    assert trips_cards[3].value == "King"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("3", "Hearts")])
    is_trips, trips_cards = hands.is_trips(player_hand)
    assert not is_trips


def test_is_two_pair():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Clubs"), Card("3", "Hearts"), Card("3", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    is_tp, tp_cards = hands.is_two_pair(player_hand)
    assert is_tp
    assert tp_cards[0].value == "Ace"
    assert tp_cards[2].value == "King"
    assert tp_cards[3].value == "King"
    assert tp_cards[4].value == "5"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("King", "Clubs"), Card("3", "Hearts"), Card("3", "Spades"),
         Card("2", "Spades"), Card("2", "Diamonds"), Card("Jack", "Hearts")])
    is_tp, tp_cards = hands.is_two_pair(player_hand)
    assert is_tp
    assert tp_cards[0].value == "3"
    assert tp_cards[2].value == "2"
    assert tp_cards[4].value == "Ace"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Diamonds"), Card("2", "Hearts"), Card("9", "Clubs"),
         Card("King", "Spades"), Card("Jack", "Diamonds"), Card("3", "Hearts")])
    is_tp, tp_cards = hands.is_two_pair(player_hand)
    assert not is_tp


def test_is_high_card():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("3", "Clubs"), Card("5", "Hearts"), Card("7", "Spades"),
         Card("9", "Spades"), Card("10", "Diamonds"), Card("King", "Hearts")])
    is_high_card, high_cards = hands.is_high_card(player_hand)
    assert is_high_card
    assert high_cards[0].value == "Ace"
    assert high_cards[1].value == "King"
    assert high_cards[2].value == "10"
    assert high_cards[3].value == "9"
    assert high_cards[4].value == "7"


def test_identify_hand():
    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("3", "Clubs"), Card("5", "Hearts"), Card("7", "Spades"),
         Card("9", "Spades"), Card("10", "Diamonds"), Card("King", "Hearts")])
    hand, best_five = hands.identify_hand(player_hand)
    assert hand == HandNames.HIGH_CARD
    assert best_five[2].value == "10"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Clubs"), Card("3", "Hearts"), Card("4", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    hand, best_five = hands.identify_hand(player_hand)
    assert hand == HandNames.STRAIGHT
    assert best_five[0].value == "5"
    assert best_five[2].value == "3"

    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Clubs"), Card("Ace", "Hearts"), Card("7", "Spades"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    hand, best_five = hands.identify_hand(player_hand)
    assert hand == HandNames.FULL_HOUSE
    assert best_five[0].value == "Ace"
    assert best_five[2].value == "Ace"
    assert best_five[3].value == "King"

    hands = init_hands()
    player_hand = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Spades"), Card("3", "Spades"), Card("4", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    hand, best_five = hands.identify_hand(player_hand)
    assert hand == HandNames.STRAIGHT_FLUSH
    assert best_five[0].value == "5"
    assert best_five[2].value == "3"
    assert best_five[3].value == "2"
    assert best_five[4].value == "Ace"


def test_compare_hands():
    player_hand1 = stack_and_sort(
        [Card("Ace", "Spades"), Card("3", "Clubs"), Card("5", "Hearts"), Card("7", "Spades"),
         Card("9", "Spades"), Card("10", "Diamonds"), Card("King", "Hearts")])
    player_hand2 = stack_and_sort(
        [Card("Ace", "Spades"), Card("2", "Clubs"), Card("3", "Hearts"), Card("4", "Spades"),
         Card("5", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    player_hand3 = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Clubs"), Card("Ace", "Hearts"), Card("7", "Spades"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])
    player_hand4 = stack_and_sort(
        [Card("Ace", "Spades"), Card("Ace", "Clubs"), Card("Jack", "Hearts"), Card("7", "Spades"),
         Card("King", "Spades"), Card("King", "Diamonds"), Card("King", "Hearts")])

    hands = init_hands()
    winners = hands.compare_hands({1: player_hand1, 2: player_hand2, 3: player_hand3, 4: player_hand4})
    assert winners == [3]