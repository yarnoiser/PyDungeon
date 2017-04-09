from math import floor
from dice import d6

def ability_modifier(score):
  return int(floor((score - 10) / 2))

def ability_roll():
  rolls = sorted([d6(), d6(), d6(), d6()])
  return sum(rolls[1:])

class Abilities():
  def __init__(self, str, dex, con, int, wis 
               , cha):
    self.str = str
    self.dex = dex
    self.con = con
    self.int = int
    self.wis = wis
    self.cha = cha

def random_abilities():
  return Abilities(ability_roll(), ability_roll(), ability_roll(),
                   ability_roll(), ability_roll(), ability_roll())


