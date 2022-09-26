import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def render_all(chx,chy):
        clear_canvas_now()
        grass.draw(400,30)
        character.draw_now(chx,chy)
        delay(0.03)

def run_circle():
    print('CLRCLE')
    

    cx,cy,r =  400,300,200
    for deg in range(-90,270+1,5):
        x = cx + r * math.cos(deg /360 * 2 * math.pi)
        y = cy + r * math.sin(deg/360 * 2 * math.pi)
        render_all(x,y)




def run_rectangle():
    print('RECCTANGLE')
    #bottom line
    for x in range(50,750+1,10):
        render_all(x,90)

    #right line
    for y in range(80,550+1,10):
        render_all(750,y)
    #top line
    for x in range(750,50-1,-10):
        render_all(x,550)
    #left line
            
    for y in range(550,76-1,-10):
        render_all(30,y)


while(True):
    
    run_rectangle()
    run_circle()
    break
    


close_canvas()
