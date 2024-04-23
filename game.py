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

# Example usage:

# Flip an unfair coin with a 70% chance of heads.
coin_flip = flip_coin()

# Print the result.
print(coin_flip)
