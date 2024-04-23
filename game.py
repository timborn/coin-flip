# TODO: graph should show we always start with the same balance.  
# Another off-by-one error

import random
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

PROBABILITY_OF_HEADS = 0.6
NFLIPS = 300
NGAMES = 1000
INITIAL_BALANCE = 25

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

### I AM A SIMPLETON
def user_bets(balance=0):
  return "heads", 5


def play_the_game():
  ### returns final balance and number of flips (watch out for fail on final)
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
    guess, bet = user_bets(balance)
  
    # a bit of error checking, please
    if (bet > balance):
      # print("you tried to bet ", bet, " but you only have ", balance)
      bet=0
  
    # Print the result.
    # print(coin_flip, guess)
    if coin_flip == guess:
      # print("win  ", end="")
      balance += bet
    else:
      # print("lose ", end="")
      balance -= bet
  
    # print(balance)
  
    balance_over_time[i] = balance
    if (balance <=0 ): 
      # print("wah wah wah.  flip #", i+1)
      break

  # return balance, i+1	# zero based iter
  return balance_over_time

def simulate_many_games(games=10):
# returns an array of arrays of the balance over time
  results = []	# it's an array - is this necessary?
  for i in range(games):
#     winnings, n = play_the_game()
#     ### TODO: what data structure to keep results so I can analyze the set?
#     print ("After ", n, " flips the final balance was ", winnings)
    results.append(play_the_game())

  # print(results)
  return results
  
### main

all_ys = simulate_many_games(NGAMES)
all_xs = [np.arange(NFLIPS, dtype='int') for _ in range(NGAMES)]

# TODO: how many simulations failed?  Seems like you can count last
# array element == 0 to see failure
broke = 0
poor = 0
for ys in all_ys:
  if ys[NFLIPS-1] == 0: broke += 1
  if ys[NFLIPS-1] < INITIAL_BALANCE: poor += 1

print("Out of ", NGAMES, " games:")
print(poor, " lost money")
print(broke, " went broke")
print((NGAMES-poor)/NGAMES, " % success")

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
