class Effect():
  INF = -1
  def __init__(self, value, max, duration):
    self.value = value
    self.max = max
    self.duration = duration

  def run(self):
    if self.duration > 0:
      self.duration -= 1

  def expired(self):
    self.duration == 0


