import os
from colorama import Fore, Back, Style
def render(map):
        for row in map:
            for col in row:
                print(Fore.BLUE + str(col),end=' ')
            print(' ')

