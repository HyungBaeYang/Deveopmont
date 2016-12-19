import json
import os

from pico2d import *

name = "EnemyBullet"

class EnemyBullet:

    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image("Missail.jpg")
        self.dir = 1

    def update(self):
        self.y -= 2
        pass

    def frame(self):
        pass

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)