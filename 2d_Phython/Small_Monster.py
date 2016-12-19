import random
from pico2d import *

from EnemyBullet import EnemyBullet

name = "Small_Monster"
BulletContainer = []
iCount = 0

TimerBool = False
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
        global iCount
        self.x += (self.dir * 5)
        if self.x < 0:
            self.dir = 1
            self.x = 0
        elif self.x > 800:
            self.dir = -1
            self.x = 800

        iCount += 1

        if iCount > 40:
            BulletContainer.append(EnemyBullet(self.x, self.y))
            iCount = 0


        for bullet in BulletContainer:
            bullet.update()
        pass

    def frame(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
        for bullet in BulletContainer:
            bullet.draw()

    def get_bb(self):
        return self.x - 50, self.y - 30, self.x + 30, self.y + 30

