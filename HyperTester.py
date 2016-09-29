# Bomberman Clone 1v1 / WARNING: Test and pseudo code sheet
import numpy as np
import sys
from queue import *
grid = [['.', '.', '.', '0', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '0', '.', '0', '.', '.', '.', '.', '.'],
        ['0', '.', '.', '0', '.', '.', '.', '.', '.', '0', '.', '.', '0'],
        ['.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
        ['0', '.', '0', '.', '.', '.', '.', '.', '.', '.', '0', '.', '0'],
        ['.', '.', '.', '.', '0', '.', '0', '.', '0', '.', '.', '.', '.'],
        ['0', '.', '0', '.', '.', '.', '.', '.', '.', '.', '0', '.', '0'],
        ['.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
        ['0', '.', '.', '0', '.', '.', '.', '.', '.', '0', '.', '.', '0'],
        ['.', '.', '.', '.', '.', '0', '.', '0', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '0', '.', '.', '.', '.', '.', '0', '.', '.', '.']]

match = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '.']

class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass
    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(
            value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start,
                                  0,
                                  self.start,
                                  self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.path

# Main
if __name__ == "__main__":
    start1 = "123456"
    goal1 = "654321"
    print("starting...")
    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("%d " %i + a.path[i])

'''
Map key:
    '0' = Box,
    '.' = empty space
* Smart pathfinder built into game already: Bot will attempt to get to the coordinates or closest one if box exists.
* Not sure if it is effective to add opponent or opponents bombs to the map
* Bomb begins with a range of 3, power upgrades in higher leagues exist
    Powerup has chance to spawn when a box is blown up
    Walk on the powerup to collect it

grid_width = 13
grid_height = 11
startPosition = 0, 0  # Coordinates we begin at x, y: 0, 0 = top left OR 12, 10 = bot right

for i in range(entities):
    entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]

# TODO: Navigate grid from start point to score the most points.

Can MOVE X Y or BOMB X Y
if owner == 1 and bombCount == 0:
    bombLocation = x, y
    The enemy has dropped a bomb and it will explode in the shape of a +, +1 in each direction of the bombs coordinate
    without upgrades.

if neighboring spaces == boxes:
    bomb current location
else:
    scan map for best position and enemy bombs so we don't die
    bombing_coordinates = good location
    move x y to good location
    if playerLocation = bombing_coordinates:
        bomb x y
'''