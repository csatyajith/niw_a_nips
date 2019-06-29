from spin_a_win import SpinAWin
import json
import itertools

spin = SpinAWin()
possible_spin_bets = [1, 2, 5, 10, 20, 40]
boxes = len(possible_spin_bets)
total_wager_per_customer = 4
rng = list(range(total_wager_per_customer + 1)) * boxes
all_possible_bets = list(set(i for i in itertools.permutations(rng, boxes) if sum(i) == total_wager_per_customer))
spins_per_customer = 10000

average_profit = list()
total_wager = 0
profit_makers = 0
for i in all_possible_bets:
    bet = {key: value for key, value in zip(possible_spin_bets, i)}
    customer_profit, investment = spin.sim_session(spins_per_customer, [bet])
    total_wager += investment
    profit_makers += 1 if customer_profit > 0 else 0
    average_profit.append({"profit": customer_profit,
                           "bet": bet})

sorted_avg = sorted(average_profit, key=lambda k: k["profit"])
profit_by_casino = 0
for iteration in sorted_avg:
    profit_by_casino -= iteration["profit"]
top_ten_spins = sorted_avg[-10:]

with open("top_ten_lucky_spins.json", "w") as sim_file:
    json.dump(top_ten_spins, sim_file)

print("Profit made by casino", profit_by_casino)
print("Total money bet in", total_wager)
print("Total number of customers who played", len(all_possible_bets))
print("Total customers making profit", profit_makers)
