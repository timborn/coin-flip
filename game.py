# TODO: range check strategy selector input from cmd line

import random
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
import sys

PROBABILITY_OF_HEADS = 0.6
NFLIPS = 300
NGAMES = 1000
INITIAL_BALANCE = 25
WINNING_BALANCE = 250	# in the original game, >=$250 is a winner

def flip_coin(probability_of_heads = PROBABILITY_OF_HEADS):
  """Flips an unfair coin with the given probability of heads.

  Args:
    probability_of_heads: A float between 0 and 1, representing the probability
      of the coin landing on heads.

  Returns:
    A string, either "heads" or "tails".
  """

  if random.random() < probability_of_heads:
    return "heads"
  else:
    return "tails"

###
### YOU ARE HERE
###
### This is your strategy for betting.
### You know your current balance.
### If needed, we could provide which flip this is, 
### and how many flips in a game.
### 
### Work out which side you like ("heads") and how much to bet.
### Return the name of the strategy, "heads", bet amt
###
def user_bets(balance, idx):
  dispatch = {
    0: user_bets_simpleton,
    1: user_bets_thirds,
    2: user_bets_cheapskate,
    3: user_bets_ten,
    4: user_bets_ten_percent
  }
  # return user_bets_simpleton(balance)
  # return user_bets_thirds(balance)
  # return user_bets_cheapskate(balance)
  # return user_bets_ten(balance)
  # return user_bets_ten_percent(balance)
  return dispatch[idx](balance)

### I AM A SIMPLETON
def user_bets_simpleton(balance):
  return "simpleton", "heads", 5

### THIRDS
def user_bets_thirds(balance):
  return "thirds", "heads", int(balance/3)

### CHEAPSKATE
def user_bets_cheapskate(balance):
  return "cheapskate", "heads", 2.50

### TEN
def user_bets_ten(balance):
  return "ten", "heads", min(10, balance)

### TEN PERCENT
def user_bets_ten_percent(balance):
  return "ten percent", "heads", int(balance/10)


def play_the_game(strat_selector):
  ### returns strategy string and balance over time (array)
  balance=INITIAL_BALANCE

  # keep track of balance for all [0..NFLIPS-1] turns
  balance_over_time = [0] * NFLIPS

  for i in range(NFLIPS):
    # when we plot, make sure it looks like we all started from the same place
    if i==0: 
      balance_over_time[i] = INITIAL_BALANCE
      continue

    # Flip an unfair coin 
    coin_flip = flip_coin()
    strategy, guess, bet = user_bets(balance, strat_selector)
  
    # a bit of error checking, please
    if (bet > balance):
      bet=0
  
    if coin_flip == guess:
      balance += bet
    else:
      balance -= bet
  
    balance_over_time[i] = balance
    if (balance <=0 ): 
      break

  # return balance, i+1	# zero based iter
  return strategy, balance_over_time

def simulate_many_games(games, strat_selector):
# returns strategy name and an array of arrays of the balance over time
  results = []	# it's an array - is this necessary?
  for i in range(games):
    strategy, ary = play_the_game(strat_selector)
    results.append(ary)

  # print(results)
  return strategy, results
  
### main

strat_selector = 0
if len(sys.argv) >= 2:
  strat_selector = int(sys.argv[1])

strategy, all_ys = simulate_many_games(NGAMES, strat_selector)
all_xs = [np.arange(NFLIPS, dtype='int') for _ in range(NGAMES)]

# some stats
broke = 0
poor = 0
winner = 0
maxm=0
print("strategy: ", strategy)
for ys in all_ys:
  if ys[NFLIPS-1] == 0: broke += 1
  if ys[NFLIPS-1] < INITIAL_BALANCE: poor += 1
  if ys[NFLIPS-1] >= WINNING_BALANCE: winner += 1
  if ys[NFLIPS-1] > maxm: maxm = ys[NFLIPS-1]

print("Out of ", NGAMES, " games:")
print(poor, " lost money")
print(broke, " went broke")
print(winner, " exceeded ", WINNING_BALANCE)
print("max final value: ", maxm)
print(((NGAMES-poor)/NGAMES)*100, " % didn't fail")
print((winner/NGAMES)*100, " % success")

# append nan to each segment
all_xs_with_nan = [np.concatenate((xs, [np.nan])) for xs in all_xs]
all_ys_with_nan = [np.concatenate((ys, [np.nan])) for ys in all_ys]

# concatinate segments into single line
xs = np.concatenate(all_xs_with_nan)
ys = np.concatenate(all_ys_with_nan)

fig = go.Figure(data=[
    go.Scattergl(x=xs, y=ys, mode='lines', opacity=0.05, line={'color': 'darkblue'})
])
plot(fig) 
