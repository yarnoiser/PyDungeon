#!/usr/bin/env python3

import sys
from sdl2 import *
import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("PyDungeon", size=(640, 480))
window.show()

while 1:
  events = sdl2.ext.get_events()
  for event in events:
    if event.type == SDL_QUIT:
      sys.exit()
  window.refresh()


