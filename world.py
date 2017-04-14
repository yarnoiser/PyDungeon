class Tile():
  def __init__(self, texture, clip=False, contents=[]):
    self.texture = texture
    self.clip = clip
    self.contents = contents

def EmptyTile():
  return Tile(None, clip=True)

class Scene():
  def __init__(self, width, height):
    self.tiles = [[EmptyTile() for tile in range(height)] for column in range(width)]

  def setTile(self, x, y, tile):
    self.tiles[x, y] = tile

  def add(self, obj, x, y):
    self.tiles[x, y].contents.append(obj)

  def locate(self, obj):
    for x in self.tiles:
      for y in x:
        for o in self.tiles[x][y].contents:
          if o is obj:
            return x, y
    return None, None

  def remove(self, obj, x=None, y=None):
    if not (x and y):
      x, y = self.locate(obj)
    if not (x and y):
      return
    self.tiles[x][y].contents = filter(lambda o: not obj is o, self.tiles[x][y].contents)

def EmptyScene():
  return Scene(0, 0)


