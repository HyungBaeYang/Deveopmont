import random
from pico2d import *

import main_state
__author__ = 'user'


iCount = 1


class Enemy:
   global Type
   global iCount
   global NHp
   global Time

   def __init__(self,x,y):
        self.x = x
        self.y = y
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        Enemy.image = load_image("resource/enemy/enemy1.png")
        self.Type = 1
        self.NHp = 2
        self.Time = 0

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            return True

        else:
            return False

   def AAA(self):
        self.Time += 1

        if(self.Time == 50):
            self.Time = 0
            return True
   def Power(self):
       self.NHp -=2
       self.Type = 2
       return True

   def Hp(self):

        self.NHp -= 1
        if(self.NHp == 0):
            #self.NHp = 3
            self.Type = 2
            return True
        else:
            return False



   def update(self):
        if(self.Type == 1):
            if(self.y >= 600):
                self.y += (self.dir * 5)
            else:
                self.x += (self.dir * 5)
                if(self.x <= 0):
                    self.dir *= -1

                elif(self.x >= 500):
                    self.dir *= -1





   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)

class Enemy2:
   global Type
   global iCount
   global BHp

   def __init__(self,x, y):
        self.x = x
        self.y = y
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        Enemy2.image = load_image("resource/enemy/boss.png")
        self.Type = 1
        self.BHp = 100

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            return True

        else:
            return False

   def Power(self):
       self.BHp -= 10
       if(self.BHp <= 0):
            self.Type = 2

   def Hp(self):
        self.BHp -= 1
        if(self.BHp == 0):
            self.Type = 2
            return True
        else:
            return False


   def update(self):
            if(self.y >= 600):
                self.y += (self.dir * 10)
            else:
                self.y = 599




   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)




class middleboss:
   global Type
   global iCount
   global MBHp

   def __init__(self,x, y):
        self.x = x
        self.y = y
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        middleboss.image = load_image("resource/enemy/중간보스.png")
        self.Type = 1
        self.MBHp = 30

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            return True

        else:
            return False

   def Hp(self):
        self.MBHp -= 1
        if(self.MBHp <= 0):
            self.Type = 2
            return True
        else:
            return False

   def Power(self):
       self.MBHp -= 10
       if(self.MBHp <= 0):
            self.Type = 2




   def update(self):
            if(self.y >= 600):
                self.y += (self.dir * 3)
            else:
                self.y = 599




   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)





