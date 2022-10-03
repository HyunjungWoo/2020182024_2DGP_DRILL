from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events_move_side():
    global side
    global running
    global dir_x
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                side = 1
                dir_x += 1
            elif event.key == SDLK_LEFT:
                side = 0
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                side = 1
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                side = 0
                dir_x += 1

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
dir_x = 0
dir_y = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
side = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame*100,side*100,100,100,x,y)
    update_canvas()


    frame = (frame + 1) % 8
    x += dir_x * 5





close_canvas()

