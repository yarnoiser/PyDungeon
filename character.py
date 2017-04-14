from math import floor
from random import shuffle
from dice import *
from combat import *

# base class for D&D statistics
# has maximum and current values, and a list of effects
# classes using must call runEffects to decrement effect counters and remove
# expired effects
class stat():
  def __init__(self, val):
    self.val = val
    self.max = val
    self.effects = []

  def inc(self, val):
    if self.val + val > self.max:
      self.val = self.max
    else:
      self.val = self.val + val

  def dec(self, val):
    self.inc(0 - val)

  def incMax(self, val):
    self.max += val

  def decMax(self, val):
    self.max -= val

  def runEffects(self):
    for effect in self.effects:
      effect.run()
      if effect.expired:
        self.max -= effect.max
        if self.val - effect.val > self.max:
          self.val = self.max
        else:
          self.val -= effec.val
    self.effects = list(filter(lambda eff: not(eff.expired), self.effects))

def abilityModifier(score):
  return int(floor((score - 10) / 2))

def abilityRoll():
  rolls = sorted([d6.roll(), D6.roll(), D6.roll(), D6.roll()])
  return sum(rolls[1:])

class Abilities(dict):
  def __init__(self, str, dex, con, int, wis 
               , cha):
    self['str'] = stat(str)
    self['dex'] = stat(dex)
    self['con'] = stat(con)
    self['int'] = stat(int)
    self['wis'] = stat(wis)
    self['cha'] = stat(cha)

  def runEffects(self):
    for ability in self:
      ability.run_effects()

def RandomAbilities():
  return Abilities(ability_roll(), ability_roll(), ability_roll(),
                   ability_roll(), ability_roll(), ability_roll())

def PrioritizedAbilities(priority):
  abilities = Abilities(0, 0, 0, 0, 0, 0)
  rolls = list(reversed(sorted([ability_roll(), ability_roll(), ability_roll()
                         , ability_roll(), ability_roll(), ability_roll()])))
  missing = set(['str', 'dex', 'con', 'int', 'wis', 'cha']) - set(priority)
  missing = list(missing)
  shuffle(missing)
  priority.extend(missing)
 
  i = 0
  while i < len(priority):
    abilities[priority[i]] = rolls[i]
    i += 1

  return abilities

def PurchasedAbilities(str, dex, con, int, wis, cha):
  purchaseTable = {-2: 8, 
                   -1: 9,
                    0: 10,
                    1: 11,
                    2: 12,
                    3: 13,
                    4: 13,
                    5: 14,
                    6: 14,
                    7: 15}

  if sum([str, dex, con, int, wis, cha]) > 15:
    raise ValueError("Points spent must not exceed total")

  return Abilities(purchaseTable[str], purchaseTable[dex], purchaseTable[con],
                   purchaseTable[int], purchaseTable[wis], purchaseTable[cha])


class Race():
  def __init__(self, speed):
    self.speed = stat(speed)

  def runEffects():
    self.speed.run_effects()

HUMAN = Race(30)

class Class():
  def __init__(self, hd):
    self.hd = hd

  def runEffects(self):
    return None

FIGHTER = Class(D10)

class Character(dict):
  def __init__(self, abilities, race, clss):
    self['abilities'] = abilities
    self['race'] = race
    self['class'] = clss
    self['inventory'] = []
    self['effects'] = []

  def runEffects(self):
    for attr in self:
      attr.run_effects()

