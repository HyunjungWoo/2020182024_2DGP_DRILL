from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('ch2_jumping.png')

str1 = 'ch2_jumping'
num = 0
str2 = '.png'

character = load_image(str1+num+str2)
x = 0
frame = 0
while(x < 800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 70,0, 74,66,x,90) #왼쪽 아래 너비 높이
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)
    get_events()





close_canvas()

