import os
from colorama import Fore, Back, Style
from app import app
def render(map):

    for row in map.map:
        for elem in row:
             elem.render()
            

        print(' ')

def renderStatus(map):
    print("Time: day")
    print("Weather: sunny")
    print("Whispers: " + app.Commands)
