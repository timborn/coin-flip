import random

def flip_coin(probability_of_heads = 0.6):
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

def user_bets(balance=0):
  return "heads", 5

def simulate_many_games(games=10):
  ### something goes here
  print("TODO")

def play_the_game():
  ### returns final balance and number of flips (watch out for fail on final)
  balance=25
  for i in range(300):
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
  
    if (balance <=0 ): 
      # print("wah wah wah.  flip #", i+1)
      break

  return balance, i+1	# zero based iter

### main
winnings, n = play_the_game()
print ("After ", n, " flips the final balance was ", winnings)
if winnings <= 0:
  print("LOSS")
