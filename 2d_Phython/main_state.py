import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    image = None

    plane_STAND ,plane_LEFT, plane_RIGHT = 0, 1, 2


    def __init__(self):
        self.x, self.y = 300, 100
        self.frame = 0
        self.image = load_image('plane.png')
        self.state = self.plane_STAND
        self.dir = 1


    def handle_stand(self):
        self.frame = 0
        self.state = self.plane_STAND
        pass
    def handle_left(self):
        self.frame = 1
        if self.x < 0:
            self.state = self.plane_LEFT
            self.x = 0
        pass
    def handle_right(self):
        self.frame = 2
        if self.x > 800:
            self.state = self.plane_RIGHT
            self.x = 800
        pass

    def update(self):
        #self.x += self.dir
        #self.frame = (self.frame + 1) % 8
        #self.frame = 0
        self.handle_state[self.state](self)
        pass


    def handle_event(self, event):
        if self.state == self.plane_STAND:
            self.frame = 0
            self.state = self.plane_STAND
        elif self.state == self.plane_LEFT:
            self.frame = 1
            self.state = self.plane_LEFT
        elif self.state == self.plane_RIGHT:
            self.state = self.plane_RIGHT
        pass

    handle_state = {
        plane_STAND: handle_stand,
        plane_LEFT: handle_left,
        plane_RIGHT: handle_right
    }
    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global boy, grass
    del (boy)
    del (grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global boy

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            boy.handle_event(event)
            boy.x -= 5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            boy.handle_event(event)
            boy.x += 5



def update():
    handle_events()
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass





