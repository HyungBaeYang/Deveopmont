import random
from pico2d import *



__author__ = 'user'

from missile import Missile1
from missile import Missile2
from missile import Missile3
import main_state


LR = 0

class character:
   global missile1,missile2,missile3, State
   image = None

   global bullet1,bullet2,bullet3

   #bullet1 = []
   bullet2 = []
   bullet3 = []

   global left
   global right
   global  up
   global down

   left = False
   right = False
   up = False
   down = False
   missile2 = Missile1(0,0)
   missile2 = Missile2(0,0)
   missile3 = Missile3(0,0)

   def __init__(self):

        self.x, self.y = 250,50
        self.State = 0
        self.missilex = self.x

        character.image = load_image("resource/character/plane.png")

    #천천히

   def handle_event(self, event):
        global mis
        global left,right,up,down, LR
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                left = True
                LR = 1
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
                right = True
                LR = 2
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_UP):
                up = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_DOWN):
                down = True
        if(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                LR = 0
                left = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_RIGHT):
                LR = 0
                right = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_UP):
                up = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_DOWN):
                down = False

   def get_bb(self):
        return self.x - 20, self.y - 10, self.x + 20, self.y - 10

   def update(self):
       global left,right,up,down, LR

       if(left == True):
           self.x -=10
           if(self.x <= 10):
               self.x = 10
       if(right == True):
           self.x +=10
           if(self.x >= 490):
               self.x = 490
       if(up == True):
           self.y +=10
           if(self.y >= 690):
               self.x = 690
       if(down == True):
           self.y -=10
           if(self.y <= 10):
               self.y = 10

       if(self.State == 1):
           self.y += 3
           if(self.y >= 100):
               self.State = 0


   def Die(self):
       if(self.State == 0):
           self.State = 1
           self.y = -10
           self.x = 250



   def draw(self):
        self.image.clip_draw(0, 200 - ( LR * 100), 100, 100, self.x, self.y)
