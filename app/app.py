from app.render import render
from app.world.tile import Tile
from os import system
def clear():
    system('clear')
def run():
    init()
    loop()
def init():
    print("Welcome!")
def rend(map):
    clear()
    render.render(map)

def logic(map):
    ans = input()
    if ans == 'plant':
        map[14][7].changeTo(',')
def loop():
    l = 16;
    h = 16;
    map = [[]] 
    for row in range(l):
        map.append([])
        for elem in range(h):
            map[row].append(Tile('\'', row, elem))
    for row in map:
        for elem in row:
            if elem.x > 13:
                elem.changeTo(':')
    


    while(True):
        rend(map)
        logic(map)
