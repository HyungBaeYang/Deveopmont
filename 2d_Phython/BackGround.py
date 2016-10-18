from pico2d import *


class BackGround:
    def __init__(self):
        self.image = load_image('Stage.png')
        #self.bDown = False
        #self.y = self.ScrollY
        self.y = 0
        #self.ScrollY = 0

    def update(self):
        self.y += 5
        print('움직')
        #if self.bDown == True:
        #    self.ScrollY += 5


    def draw(self):
        self.image.draw(400, 4000 - self.y, 800, 8030)



