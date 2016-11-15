import random
import json
import os

from pico2d import *
import Bullet
import game_framework
import title_state
import Boy
import BackGround
from Small_Monster import Small_Monster


name = "MainState"

boy = None
grass = None
font = None


def enter():
    global boy, backGround, mop

    global Small_Monster
    boy = Boy.Boy()
    mop = [Small_Monster(100 + (75 * i), 500) for i in range(4)]
    backGround = BackGround.BackGround()
    pass


def exit():
    global boy, grass
    del (boy)
    del (mop)
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

def update():
    boy.update()
    for mob in mop:
        mob.update()
    backGround.update()
    for bull in boy.GetBullet():
        for mons in mop:
            if collide(mons, bull):
                boy.GetBullet().remove(bull)
                mop.remove(mons)

    pass


def draw():
    clear_canvas()
    backGround.draw()
    boy.draw()
    for mob in mop:
        mob.draw()
    update_canvas()
    pass




def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


