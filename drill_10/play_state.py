from pico2d import *
import game_framework
import title_state
import item_state
import boy_adjust_state
import random
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 90
        self.frame = random.randint(0,7)
        self.image = load_image('animation_sheet.png')
        self.dir = 1 #오른쪽
        self.item = None
        self.ball_image =load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')


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

        if self.item == 'Ball':
            self.ball_image.draw(self.x+10,self.y+50)
        elif self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                #game_framework.change_state(title_state)
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(boy_adjust_state)
    delay(0.01)
#boy = None
boys =[] #여러 명의 소년들 
grass = None
running = True


#초기화
def enter():
    global grass,running
    boys.append(Boy())
   
    grass = Grass()
    running = True


# finalization code
def exit():
    global grass
    for boy in boys:
        del boy
    del grass

def update():
    for boy in boys:
        boy.update()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()


def pause():
    pass
def resume():
    pass

def add_one_boy():
    boys.append(Boy())

def delete_one_boy():
    if len(boys)>=2:
        boys.pop()

def set_all_boys_items(item):
    for boy in  boys:
        boy.item = item