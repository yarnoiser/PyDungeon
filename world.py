class Tile():
  def __init__(self, texture, clip=False, contents=[]):
    self.texture = texture
    self.clip = clip
    self.contents = contents

def Empty_tile():
  return Tile(None, clip=true)


