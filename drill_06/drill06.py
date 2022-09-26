from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x = x+2
    delay(0.01)

y = 30

while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(790,y)
    y = y+2
    delay(0.01)



while(0<x<=800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,600)
    x = x-2
    delay(0.01)


y =600

while(30<y<=600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,y)
    y = y-2
    delay(0.01)


# fill here

close_canvas()
