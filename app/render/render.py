import os
from colorama import Fore, Back, Style
def render(map):
    for row in map:
        for elem in row:
             elem.render()
            

        print(' ')


