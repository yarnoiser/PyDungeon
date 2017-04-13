# Implementation of randbelow from python 3.6's secrets module
# Copyright © 2001-2017 Python Software Foundation; All Rights Reserved
from random import SystemRandom

_sysrand = SystemRandom()

def randbelow(exclusive_upper_bound):
  """Return a random int in the range [0, n)."""
  if exclusive_upper_bound <= 0:
    raise ValueError("Upper bound must be positive.")
  return _sysrand._randbelow(exclusive_upper_bound)
# End of python software foundation code
# ====================================================================

class Die():
  def __init__(self, sides):
    self.sides = sides

  def roll(self):
    return randbelow(self.sides) + 1

D4 = Die(4)
D6 = Die(6)
D8 = Die(8)
D10 = Die(10)
D12 = Die(12)
D20 = Die(20)
D100 = Die(100)

