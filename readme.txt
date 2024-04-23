Tue Apr 23 02:53:55 MST 2024
----------------------------

Elm Wealth's Coin Flip Challenge is a game on elmwealth.com where
players test their skill at betting on heads or tails after flipping
a biased coin. The coin is programmed to have a 60% chance of coming
up heads, and players can bet any amount of money in their balance
on each flip.

Start with $25.  Game over when you get to zero.  n=300 flips

https://elmwealth.com/coin-flip/

Getting Started

#? one-off crap to create an env in git
#? python3 -m venv --prompt "pyenv> " env
#? git init
#? echo 'env' > .gitignore	# the env folder we just created is not in git

git clone repo
source env/bin/activate	# to start using the environment
deactivate		# to stop  using the environment
pip install <pkg>	# done while inside env
pip freeze > requirements.txt	# outside env?  top level?  
pip install -r requirements.txt	# install all needed pkgs
