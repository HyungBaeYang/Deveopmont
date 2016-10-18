import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Boy
import BackGround


name = "MainState"

boy = None
grass = None
font = None





def enter():
    global boy, backGround
    boy = Boy.Boy()
    backGround = BackGround.BackGround()
    pass


def exit():
    global boy, grass
    del (boy)
    del (backGround)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            boy.handle_events(event)
    pass
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
         #   boy.handle_event(event)
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
         #   boy.handle_event(event)

def update():
    boy.update()
    backGround.update()
    pass


def draw():
    clear_canvas()
    backGround.draw()
    boy.draw()
    update_canvas()
    pass





