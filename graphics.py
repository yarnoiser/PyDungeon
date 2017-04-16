import sys
import os
from sdl2 import *
import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("PyDungeon", size=(640, 480))
window.show()

textures = {}

for f in os.listdir("./Textures"):
  if os.path.isfile(f):
    textures[os.path.splitext(f)[0]] = sdl2.ext.load_image(f)

def loop():
  while 1:
    events = sdl2.ext.get_events()
    for event in events:
      if event.type == SDL_QUIT:
        sys.exit()
    window.refresh()


