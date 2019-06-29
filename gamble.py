from spin_a_win import SpinAWin

spin_a_win = SpinAWin()

bets = [{5: 1, 10: 1, 20: 1, 40: 1}]
profit = spin_a_win.sim_session(200, bets)
print(profit)
