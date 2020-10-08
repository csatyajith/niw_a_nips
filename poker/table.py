import numpy as np


class Seat:
    def __init__(self):
        self.player = None
        self.occupied = False

    def sit(self, player):
        self.player = player
        self.occupied = True

    def stand(self):
        self.player = None
        self.occupied = False


class Table:
    def __init__(self, n_players, max_buy_in=np.inf):
        self.n_players = n_players
        self.max_buy_in = max_buy_in
        self.seats = [Seat() for _ in range(n_players)]
        self.n_seats_occupied = 0

    def player_sit(self, player, buy_in_amount: int):
        if buy_in_amount > self.max_buy_in:
            raise ValueError("Buy in amount over the limit allowed on this table")
        if self.n_seats_occupied > self.n_players:
            raise ValueError("No seats available on this table")
        for seat in self.seats:
            if seat.occupied is False:
                seat.sit(player)
                self.n_seats_occupied += 1
                return seat

    def player_stand(self, player):
        player.seat.stand()
        self.n_seats_occupied -= 1
