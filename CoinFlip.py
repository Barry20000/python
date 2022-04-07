from random import random

def flip_Coin():
  if random() > 0.5:
    return ("Heads")
  else:
    return ("Tails")

print(flip_Coin())
