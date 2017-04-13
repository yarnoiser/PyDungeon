from math import floor
from random import shuffle
from dice import *

class stat():
  def __init__(self, val):
    self.val = val
    self.max = val
    self.effects = []

  def __add__(self, val):
    return self.val + val

  def __sub__(self, val):
    return self.val - val

  def __mul__(self, val):
    return self.val * val

  def __matmul__(self, val):
    return NotImplemented

  def __truediv__(self, val):
    return self.val // val

  def __floordiv__(self, val):
    return self.val // val

  def __mod__(self, val):
    return self.val % val

  def __divmod__(self, val):
    return self.val / val, self % val

  def __pow__(self, val):
    return self.val ** val

  def __lshift__(self, val):
    return self.val << val

  def __rshift__(self, val):
    return self.val >> val

  def __and__(self, val):
    return self.val and val

  def __xor__(self, val):
    return self.val ^ val

  def __or__(self, val):
    return self.val or val

  def __iadd__(self, val):
    if self + val > self.max:
      self.val = self.max
    else:
      self.val += val

  def __isub__(self, val):
    self += 0 - val


  def apply_effect(self, effect):
    self.effects.append(effect)
    self.max += effect.max
    self.val += effect.value

  def run_effects(self):
    for effect in self.effects:
      effect.run()
      if effect.expired:
        self.max -= effect.max
        if self.val - effect.val > self.max:
          self.val = self.max
        else:
          self.val -= effec.val
    self.effects = list(filter(lambda eff: not(eff.expired), self.effects))

def ability_modifier(score):
  return int(floor((score - 10) / 2))

def ability_roll():
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

  def run_effects(self):
    for ability in self:
      ability.run_effects()

def random_abilities():
  return Abilities(ability_roll(), ability_roll(), ability_roll(),
                   ability_roll(), ability_roll(), ability_roll())

def prioritized_abilities(priority):
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

def purchased_abilities(str, dex, con, int, wis, cha):
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

  def run_effects():
    self.speed.run_effects()

HUMAN = Race(30)

 Class():
  def __init__(self, hd):
    self.hd = hd

  def run_effects(self):
    return None

FIGHTER = Class(D10)

class Character(dict):
  def __init__(self, abilities, race, clss):
    self['abilities'] = abilities
    self['race'] = race
    self['class'] = clss
    self['inventory'] = []
    self['effects'] = []

  def run_effects(self):
    for attr in self:
      attr.run_effects()


