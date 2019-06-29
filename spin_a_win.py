import numpy as np


class SpinAWin:
    def __init__(self):
        self.spin_results = [10, 1, 'm7', 1, 2, 1, 20, 1, 2, 5, 1, 2, 1, 10, 1, 5, 1, 2, 1, 2, 40, 1, 2, 1, 2, 5, 1, 2, 10,
                        1, 'm2', 1, 5, 2, 1, 20, 1, 2, 1, 5, 1, 10, 1, 2, 5, 1, 2, 1, 2, 5, 1, 2, 1, 2]
        self.multiplier_results = ["m7", "m2"]

    def perform_spin(self, bets: dict):
        spin_active = True
        multiplier = 1
        spin_result = None
        winnings = 0
        while spin_active:
            spin_result = self.spin_results[np.random.randint(0, len(self.spin_results))]
            if spin_result in self.multiplier_results:
                multiplier = multiplier*int(spin_result[1])
                continue
            if spin_result in bets.keys():
                winnings = (spin_result * multiplier * bets[spin_result]) + bets[spin_result]
            spin_active = False
        return spin_result, multiplier, winnings

    def sim_session(self, n_spins, bets: list):
        investment = 0
        total_winnings = 0
        for i in range(n_spins):
            if len(bets) == n_spins:
                investment += sum(bets[i].values())
                _, _, winnings = self.perform_spin(bets[i])
            elif len(bets) == 1:
                investment += sum(bets[0].values())
                _, _, winnings = self.perform_spin(bets[0])
            else:
                raise ValueError("Expected bets to be either length of spins or length 1")
            total_winnings += winnings
        profit = total_winnings - investment
        return profit, investment
