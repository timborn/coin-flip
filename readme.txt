Tue Apr 23 02:53:55 MST 2024
----------------------------

Elm Wealth's Coin Flip Challenge is a game on elmwealth.com where
players test their skill at betting on heads or tails after flipping
a biased coin. The coin is programmed to have a 60% chance of coming
up heads, and players can bet any amount of money in their balance
on each flip.

Start with $25.  Game over when you get to zero.  n=300 flips

https://elmwealth.com/coin-flip/
See Also: The Missing Billionaires (book)

Getting Started
===============

### one-off crap to create an env in git
#? python3 -m venv --prompt "pyenv> " env
#? git init
#? echo 'env' > .gitignore	# the env folder we just created is not in git

### clean start, new machine
git clone repo
pip install -r requirements.txt	# install all needed pkgs

### typical usage pattern
source env/bin/activate	# to start using the environment
pip install <pkg>	# done while inside env
pip freeze > requirements.txt	# top level, above env!
deactivate		# to stop  using the environment

Developer Notes
===============
My intention is to create a simulation with zero human intervention.
The algorithm that decides how much to bet each time is written in a 
function that returns: heads/tails and amount to bet.

The results will be how many flips you survived, and if all of them, 
how much money you had left.

Extra credit to run swarms and graph the balances, ala Monte Carlo.
