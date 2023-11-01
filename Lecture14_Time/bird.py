from pico2d import *
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ATCION = 14

FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ATCION

class Bird():
    image = None
    def __init__(self):
        self.x = random.randint(300, 1600)
        self.y = random.randint(300, 600)
        self.frame = 0
        self.frame_x = 0
        self.frame_y = 2
        self.ruler_image = load_image('ruler.png')
        self.dir = 1
        self.size_x = 180
        self.size_y = 170
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

    def update(self):
        self.frame = int(self.frame + FRAMES_PER_ATCION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.frame_x = self.frame % 5
        self.frame_y = self.frame // 5


        if self.x >= 1600 - self.size_x // 2:
            self.dir = -1
        if self.x <= 0 + self.size_x // 2:
            self.dir = 1

    def draw(self):
        if self.dir >= 1:
            self.image.clip_draw(self.frame_x * self.size_x, self.frame_y * self.size_y, self.size_x, self.size_y, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame_x * self.size_x, self.frame_y * self.size_y, self.size_x, self.size_y, 0, 'h',self.x, self.y, self.size_x, self.size_y)
