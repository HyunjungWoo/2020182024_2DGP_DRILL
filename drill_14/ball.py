import random
from pico2d import *
import game_world
import game_framework
import server
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(100, 1180), random.randint(100, 924), 0

    def get_bb(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        
        return sx - 10, sy - 10, sx + 10, sy + 10

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx,sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0

    def handle_collision(self, other, group):
        game_world.remove_object(self)

class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 500, random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

