import random
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

PROBABILITY_OF_HEADS = 0.6
NFLIPS = 300
NGAMES = 5

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
  

def play_the_game():
  ### returns final balance and number of flips (watch out for fail on final)
  balance=25

  # keep track of balance for all [0..NFLIPS-1] turns
  balance_over_time = [0] * NFLIPS

  for i in range(NFLIPS):
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

### main
# winnings, n = play_the_game()
# print ("After ", n, " flips the final balance was ", winnings)
# if winnings <= 0:
#   print("LOSS")

all_ys = simulate_many_games(NGAMES)
# all_xs = [np.arange(100, dtype='float64') for _ in range(N)]
all_xs = [np.arange(NFLIPS, dtype='int') for _ in range(NGAMES)]


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
