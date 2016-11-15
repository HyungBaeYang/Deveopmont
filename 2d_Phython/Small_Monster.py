import random
from pico2d import *

name = "Small_Monster"

class Small_Monster:

    image = None
    global running

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = -1
        self.hp = 5


        self. image = load_image('Small_Monster.png')

    def update(self):
        self.x += (self.dir * 5)
        if self.x < 0:
            self.dir = 1
            self.x = 0
        elif self.x > 800:
            self.dir = -1
            self.x = 800
        pass

    def frame(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

