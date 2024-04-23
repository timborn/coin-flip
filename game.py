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
  return "heads", 10

# Example usage:

balance=25
for i in range(10):
  # Flip an unfair coin 
  coin_flip = flip_coin()
  guess, bet = user_bets(balance)

  # Print the result.
  # print(coin_flip, guess)
  if coin_flip == guess:
    print("win")
    balance += bet
  else:
    print("lose")
    balance -= bet

  print(balance)
