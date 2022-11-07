from pico2d import *
import game_framework
import random
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0 )
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#이미지
TIME_PER_ACTION =0.3
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION =6


class Bird:
    image = None
    def __init__(self):
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.x, self.y = random.randint(0, 1600-1), 500
        self.dir = 1
        if Bird.image == None:
            self.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        print('%d' %self.x)

        if self.x > 1600:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %6


        self.x = clamp(0, self.x, 1600)



    def draw(self):
        # self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100,
        #                                3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)
        if self.dir==1:
            self.image.clip_composite_draw(int(self.frame)*180,160*0,180,150,0,'n',self.x,self.y,180//2,180//2)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 180, 160 * 0, 180, 150, 0, 'h', self.x, self.y, 180 // 2,
                                           180 // 2)
