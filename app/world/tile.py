from colorama import Fore, Back, Style
class Tile:
    
    def __init__(self, type, desc, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.parent = self
        self.desc=desc
        self.selected = False
    def setParent(self, parent):
        self.parent = parent
    def setChild(self, child):
        self.child = child

    def changeTo(self, typeTo, desc):
        self.type = typeTo
        self.desc = desc
    def render(self):
        selectModifier = ''
        if self.selected == True:
            selectModifier = Back.WHITE + Style.BRIGHT
        if self.type == '\'':
            print(selectModifier + Fore.BLUE + Style.BRIGHT + self.type, end=' ')
        elif self.type == '|' or self.type == '\\' or self.type == '/' or self.type == '-':
            print(selectModifier + Fore.YELLOW + Style.DIM + self.type, end=' ')
        elif self.type == ',':
            print(selectModifier + Fore.GREEN+self.type, end=' ')
        elif self.type == ':':
            print(selectModifier + Fore.MAGENTA + Style.BRIGHT + self.type, end = ' ')
        elif self.type == 'o':
            print(selectModifier + Fore.YELLOW + Style.DIM + self.type, end = ' ')
        else:
            print(selectModifier + Fore.CYAN + Style.DIM + self.type, end=' ')
        print(Style.RESET_ALL, end='')
