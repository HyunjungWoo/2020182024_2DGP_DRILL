from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
def draw_right():
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()

def draw_left():
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

def handle_events_move_side():
    global running
    global dir_x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                draw_right()
                dir_x += 1
            elif event.key == SDLK_LEFT:
                draw_left()
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                draw_right()
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                draw_left()
                dir_x += 1

'''def handle_events_move_updown():

    global running
    global dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                draw_right()
                dir_y += 1
            elif event.key == SDLK_DOWN:
                draw_left()
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                draw_right()
                dir_y += 1
            elif event.key == SDLK_DOWN:
                draw_left()
                dir_y -= 1

'''

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
dir_x = 0
#dir_y = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    handle_events_move_side()
    #handle_events_move_updown()
    frame = (frame + 1) % 8
    x += dir_x * 5
    #y += dir_y * 5




close_canvas()




