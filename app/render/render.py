import os
from colorama import Fore, Back, Style
from app import app

def render(map):
    for row in map.map:
        for elem in row:
             elem.render()
            

        print(' ')

def renderSelect(tile):
    print()
    print('Info from cursor: ', end='')
    print(tile, end='')
def renderStatus(map):

    print('Year:', map.year)
    print('Weather:', map.weather)
    print('Whispers: ', end='')
    for command in app.Command:
        print(command.value, end=', ')
    renderSelect(map.getSelectedTile().desc)
    print('')
