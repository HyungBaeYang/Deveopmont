import random
import json
import os


from pico2d import *

import game_framework


name = "Boy"


class Boy:
    image = None
    global running

    (plane_STAND ,plane_LEFT, plane_RIGHT) = (0, 1, 2)

    MOVE = None
    PUSHLEFT = None
    PUSHRIGHT = None

    def __init__(self):
        self.x, self.y = 300, 100
        self.frame = 0
        self.image = load_image('plane.png')
        self.state = self.plane_STAND
        self.dir = 1
        self.MOVE = False

#    def handle_stand(self):
#        self.state = self.plane_STAND
#        pass
#    def handle_left(self):
#        if self.x < 0:
#            self.state = self.plane_LEFT
#            self.x = 0
#        pass
#    def handle_right(self):
#        if self.x > 800:
#            self.state = self.plane_RIGHT
#            self.x = 800
#        pass

    def update(self):
        self.states()
        self.frames()
        delay(0.01)

        pass

#    handle_state = {
#        plane_STAND: handle_stand,
#        plane_LEFT: handle_left,
#        plane_RIGHT: handle_right
#    }

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
   #     if self.state == self.plane_STAND:
   #         print('S')
   #         self.frame = 0
   #         if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
   #             self.state = self.plane_LEFT
   #             print('L')
   #             self.frame = 1
   #             self.x -= self.dir
   #         elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
   #             self.state = self.plane_RIGHT
   #             print('R')
   #             self.frame = 2
   #             self.x += self.dir
   #         else:
   #             self.state = self.plane_STAND

    def states(self):
        if self.MOVE == True:
            if self.PUSHLEFT == True:
                self.state = self.plane_LEFT
            elif self.PUSHRIGHT == True:
                self.state = self.plane_RIGHT
        elif self.MOVE == False:
            if self.PUSHLEFT == False:
                self.state = self.plane_STAND
            elif self.PUSHRIGHT == False:
                self.state = self.plane_STAND

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


