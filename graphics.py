import sys
import os
from sdl2 import *
import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("PyDungeon", size=(640, 480))

textures = {}

for f in os.listdir("./Textures"):
  fullPath = "./Textures/" + f
  if os.path.isfile(fullPath):
    textures[os.path.splitext(f)[0]] = sdl2.ext.load_image(fullPath)

def loop():
  window.show()
  while 1:
    events = sdl2.ext.get_events()
    for event in events:
      if event.type == SDL_QUIT:
        sys.exit()
    window.refresh()


