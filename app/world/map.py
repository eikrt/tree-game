from enum import Enum
from .tile import Tile

class Map:
    def __init__(self, w,h):
        self.w = w
        self.h = h
        self.seedLoc = (14,7)
        self.selectLoc = [self.seedLoc[0], self.seedLoc[1]]
        self.map = [[]]
        self.weather = Weather.SUNNY.value
        self.year = 0
        for row in range(self.w):
            self.map.append([])
            for elem in range(self.h):
                self.map[row].append(Tile('\'', 'void',row, elem))
        for row in self.map:
            for elem in row:
                if elem.x > 13:
                    elem.changeTo(':', 'dirt')

    def plant(self):
        self.map[self.seedLoc[0]][self.seedLoc[1]].changeTo(',', 'seed')
    def grow(self):
        self.selectLoc[0]-=1
        self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('|', 'wood')
        self.select(self.selectLoc[0], self.selectLoc[1])
    def branch(self, dir):
        if dir == 'left':
            if self.map[self.selectLoc[0]][ self.selectLoc[1]].type == '|':
                parent = self.map[self.selectLoc[0]][self.selectLoc[1]]
                self.moveSelect('left')
                self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('-', 'branch pointing left')
                self.map[self.selectLoc[0]][self.selectLoc[1]].setParent(parent)
                self.select(self.selectLoc[0], self.selectLoc[1])
        elif dir == 'right':
            if self.map[self.selectLoc[0]][ self.selectLoc[1]].type == '|':
                parent = self.map[self.selectLoc[0]][self.selectLoc[1]]
                self.moveSelect('right')
                self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('-', 'branch pointing right')
                self.map[self.selectLoc[0]][self.selectLoc[1]].setParent(parent)
                self.select(self.selectLoc[0], self.selectLoc[1])
    def moveSelect(self, dir):
        if dir == 'left':
            self.selectLoc[1] -= 1 
        if dir == 'right':
            self.selectLoc[1] += 1 
        if dir == 'down':      
            self.selectLoc[0] += 1 
        if dir == 'up':
            self.selectLoc[0] -= 1
        self.select(self.selectLoc[0],self.selectLoc[1])
    def select(self, x,y):
        for row in self.map:
            for elem in row:
                elem.selected = False

        self.selectLoc[0] = x
        self.selectLoc[1] = y

        self.map[x][y].selected = True
    def getSelectedTile(self):
        return self.map[self.selectLoc[0]][self.selectLoc[1]]
class Weather(Enum):
    SUNNY = 'sunny'
