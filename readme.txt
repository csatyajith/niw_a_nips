Hello there!

I recently stumbled across a gambling game on bet365. It was called Spin A Win.
The game basically goes like this:
- A wheel with a pointer is split into 54 possible outcomes
- The outcomes are 1, 2, 5, 10, 20, 40, 2 multipliers
- You can bet on any number of outcomes.
- The wheel is spun and if the pointer stops on the number you bet on, you win the outcome multiplied by your wager.
- If the pointer does on your number, you
- Eg: Suppose you bet $2 on 5 and $3 on 10. Suppose the wheel lands on 5:
    You win: 5*2 = $10
    You lose: $3
    Net profit: $7

The catch here is that you are always at a disadvantage. The payout rate is always less than the bet rate.
The only exception is the multiplier. When the pointer lands on the multiplier, the next spin has every outcome
multiplied by the multiplier value. So this means that only spins after multipliers have a positive net payout rate.

I wrote this program to demonstrate the following:

- There is no "known strategy" to make money on this game. No matter what technique you follow, you will probably end up
    losing money
- I export 10 most lucky spins for every iteration. It can be observed that these 10 spins almost always keep changing.
    Thus proving that there's no winning strategy to this game.
- I print out the amount of money the casino gains at the end of all iterations. This is "YOUR" money.
