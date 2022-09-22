from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

 while(x<400)
    y = math.sin(x/360*2*math.pi)
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
