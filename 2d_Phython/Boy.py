import random
import json
import os

from pico2d import *
from Bullet import Bullet

import game_framework


name = "Boy"
bulletCon = []

class Boy:
    image = None
    global running

    (plane_STAND ,plane_LEFT, plane_RIGHT, plane_Bullet) = (0, 1, 2, 3)
    MOVE = None
    PUSHLEFT = None
    PUSHRIGHT = None

    def __init__(self):
        self.x, self.y = 300, 100
        self.frame = 0
        self.image = load_image('plane.png')
        self.state = self.plane_STAND
        self.dir =  1
        self.MOVE = False

    def update(self):
        self.states()
        self.frames()
        delay(0.01)
        for Bul in bulletCon:
            Bul.update()
        pass


    def handle_events(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.MOVE = True
            self.PUSHLEFT = True
            self.PUSHRIGHT = False
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.MOVE = True
            self.PUSHRIGHT = True
            self.PUSHLEFT = False
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.MOVE = False
            self.PUSHLEFT = False
            self.PUSHRIGHT = False
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.MOVE = False
            self.PUSHLEFT = False
            self.PUSHRIGHT = False
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            bulletCon.append(Bullet(self.x, self.y))

    def states(self):
        if self.MOVE == True:
            if self.PUSHLEFT == True:
                self.state = self.plane_LEFT
                #self.state = self.plane_RIGHT
            if self.PUSHRIGHT == True:
                self.state = self.plane_RIGHT
        elif self.MOVE == False:
            if self.PUSHLEFT == False:
                self.state = self.plane_STAND
            elif self.PUSHRIGHT == False:
                self.state = self.plane_RIGHT

    def frames(self):
        if self.state == self.plane_STAND:
            #self.frame = 2
            self.state = 2
            #self.frame = 0
        elif self.state == self.plane_LEFT:
            self.x -= 5
            self.state = 1
            #self.frame = (self.frame - 1) % 1
            #self.frame = 2
        elif self.state == self.plane_RIGHT:
            self.x += 5
            print('R')
            self.state = 0
            #self.frame = (self.frame + 1) % 1
            #self.frame = 1


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        for Bul in bulletCon:
            Bul.draw()

    def GetBullet(self):
        return bulletCon



