from nim import *


game = Nim()
player = NimAI()

  # Keep track of current state and action
state = game.piles.copy()
action = player.choose_action(game.piles)

print(player.choose_action(state))