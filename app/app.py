from app.render import render
from app.world.tile import Tile
from app.world.map import Map
from os import system
from enum import Enum
def clear():
    system('clear')
def run():
    init()
    loop()
def init():
    print("")
def rend(map):
    clear()
    print("")
    render.render(map)
    render.renderStatus(map)
def logic(map):
    ans = input()
    if ans == Command.PLANT.value:
        map.plant()
    elif ans == Command.GROW.value:
        map.grow()
    elif ans == Command.BRANCHLEFT.value:
        map.branch('left')
    elif ans == Command.BRANCHRIGHT.value:
        map.branch('right')

def loop():
    l = 16;
    h = 16;
    map = Map(16,16)


    while(True):
        rend(map)
        logic(map)


class Command(Enum):
    PLANT = 'plant'
    GROW = 'grow'
    BRANCHLEFT = 'branchleft'
    BRANCHRIGHT = 'branchright'
