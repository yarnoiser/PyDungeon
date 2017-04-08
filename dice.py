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

def d(n):
  return randbelow(n) + 1

def d4():
  return d(4)

def d6():
  return d(6)

def d8():
  return d(8)

def d10():
  return d(10)

def d12():
  return d(12)

def d20():
  return d(20)

def d100():
  return d(100)


