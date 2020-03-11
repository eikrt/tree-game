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
                self.map[row].append(Tile('\'', row, elem))
        for row in self.map:
            for elem in row:
                if elem.x > 13:
                    elem.changeTo(':')
    def plant(self):
        self.map[self.seedLoc[0]][self.seedLoc[1]].changeTo(',')
    def grow(self):
        self.selectLoc[0]-=1
        self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('|')
        self.select(self.selectLoc[0], self.selectLoc[1])
    def branch(self, dir):
        if dir == 'left':
            parent = self.map[self.selectLoc[0]][self.selectLoc[1]]
            self.selectLoc[1]-=1
            self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('-')
            self.map[self.selectLoc[0]][self.selectLoc[1]].setParent(parent)
            self.select(self.selectLoc[0], self.selectLoc[1])
        elif dir == 'right':
            parent = self.map[self.selectLoc[0]][self.selectLoc[1]]
            self.selectLoc[1]+=1
            self.map[self.selectLoc[0]][self.selectLoc[1]].changeTo('-')
            self.map[self.selectLoc[0]][self.selectLoc[1]].setParent(parent)
            self.select(self.selectLoc[0], self.selectLoc[1])
    def select(self, x,y):
        for row in self.map:
            for elem in row:
                elem.selected = False

        self.selectLoc[0] = x
        self.selectLoc[1] = y

        self.map[x][y].selected = True
class Weather(Enum):
    SUNNY = 'sunny'
