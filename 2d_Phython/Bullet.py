import json
import os

from pico2d import *

import game_framework
name = "Bullet"



class Bullet:
    image = None
    global runnig

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('Basic_Bullet.png')

        self.dir = 1

    def update(self):
        self.y +=  10

        pass

    def frame(self):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)




