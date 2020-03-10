from colorama import Fore, Back, Style
class Tile:
    
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
    def changeTo(self, typeTo):
        self.type = typeTo
    def render(self):
        if self.type == '\'':
            print(Fore.BLUE + Style.BRIGHT + self.type, end=' ')
        elif self.type == '|' or self.type == '\\' or self.type == '/':
            print(Fore.YELLOW + Style.DIM + self.type, end=' ')
        elif self.type == ',':
            print(Fore.GREEN+self.type, end=' ')
        elif self.type == ':':
            print(Fore.MAGENTA + Style.BRIGHT + self.type, end = ' ')
        elif self.type == 'o':
            print(Fore.YELLOW + Style.DIM + self.type, end = ' ')
        else:
            print(Fore.CYAN + Style.DIM + self.type, end=' ')
        print(Style.RESET_ALL, end='')
