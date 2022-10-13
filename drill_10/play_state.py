from pico2d import *
import game_framework
import title_state
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir = 1 #오른쪽

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 5
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir ==1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    delay(0.01)
boy = None
grass = None
running = True


#초기화
def enter():
    global boy,grass,running
    boy = Boy()
    grass = Grass()
    running = True


# finalization code
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()
def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


