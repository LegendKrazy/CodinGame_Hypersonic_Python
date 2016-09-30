# Bomberman Clone 1v1 / WARNING: Test and pseudo code sheet
import numpy as np
import sys
import math
from queue import *
import sys
width, height, my_id = [int(i) for i in input().split()]
turns = 0
startPos = 0
beginPos = False
newPos = 0


grid =  \
        [['.', '.', '.', '0', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
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

textmap = [[x for x in input()] for y in range(height)]

# print("Lines: ",lines[1])
# assert ['bad width' for x in lines if len(x) != len(lines[0])] == [], "WORLD string needs to be rectangular."
def getWorldFromTextMap(textmap):
    # Converts the programmer-friendly version of a world typed out as ascii
    # characters in a multiline string into a source code-friendly version
    # that lets us access the map as world[x][y].
    worldWidth = len(textmap[0])
    worldHeight = len(textmap)
    world = []
    for i in range(worldWidth):
        world.append([''] * worldHeight)
    for x in range(worldWidth):
        for y in range(worldHeight):
            world[x][y] = textmap[y][x]
    return world

def printWorld(world):
    worldWidth = len(world)
    worldHeight = len(world[0])

    for y in range(worldHeight):
        for x in range(worldWidth):
            sys.stdout.write(world[x][y])
        sys.stdout.write('\n')

def floodFill(world, x, y, oldChar, newChar):
    # The recursive algorithm. Starting at x and y, changes any adjacent
    # characters that match oldChar to newChar.
    worldWidth = len(world)
    worldHeight = len(world[0])

    if oldChar == None:
        oldChar = world[x][y]

    if world[x][y] != oldChar:
        # Base case. If the current x, y character is not the oldChar,
        # then do nothing.
        return

    # Change the character at world[x][y] to newChar
    world[x][y] = newChar

    # Recursive calls. Make a recursive call as long as we are not on the
    # boundary (which would cause an Index Error.)
    if x > 0:  # left
        floodFill(world, x - 1, y, oldChar, newChar)

    if y > 0:  # up
        floodFill(world, x, y - 1, oldChar, newChar)

    if x < worldWidth - 1:  # right
        floodFill(world, x + 1, y, oldChar, newChar)

    if y < worldHeight - 1:  # down
        floodFill(world, x, y + 1, oldChar, newChar)

def main():
    world = getWorldFromTextMap(textmap)

    print("1: ", printWorld(world), file=sys.stderr)


    floodFill(world, 5, 8, None, '+')
    print(printWorld(world), file=sys.stderr)

    floodFill(world, 0, 0, None, 's')
    print(printWorld(world), file=sys.stderr)


if __name__ == '__main__':
    main()

def start_pos(x,y):
    # Identify where we started
    startPos = x,y
    beginPos = True
    print("Set Pos: ", startPos, file=sys.stderr)
    print("Begin Pos: ", beginPos, file=sys.stderr)

def moved_self(x,y):
    beginPos = False
    newPos = x,y
    print("moved_self: ", beginPos, file=sys.stderr)

def getSafe(x,y): # Check if character is in range and in danger, if yes MOVE to safety
    print("getSafe:", x, y, file=sys.stderr)
    print("It worked")
    '''
    if newPos[0] and newPos[1] == (x,y):
        pass
    if newPos[0] and newPos[1] == (x+1,y+1):
        pass
    if newPos[0] and newPos[1] == (x-1,y-1):
        pass
    if newPos[0] and newPos[1] == (x+2,y+2):
        pass
    if newPos[0] and newPos[1] == (x-2,y-2):
        pass
    if newPos[0] and newPos[1] == (x+3,y+3):
        pass
    if newPos[0] and newPos[1] == (x-3,y-3):
        pass
    else:
        pass
    '''
# game loop for Bomberman clone contest: 400 turns and it ends
while True:
    turns += 1
    # print("Turn: ",turns, file=sys.stderr)
    textmap = [[x for x in input()] for y in range(height)]  # a list of lists to show what is on the board
    # turn textwall into coordinates
    match = [(i, j) for i, row in enumerate(textwall) for j, cell in enumerate(row) if cell == '.']
    # print(match, file=sys.stderr)

    # Current loop game information
    entities = int(input())
    for i in range(entities):
        entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]
        if owner == 1 and bombCount == 0:
            # Detects if they dropped a bomb on the current tile
            getSafe(x,y)
            bombLocation = (x,y)
            print("bombLocation: ", bombLocation, file=sys.stderr)
        if owner == 0 and turns <= 1:  # ONLY on Turn 1 assign our starting position
            start_pos(x, y)
        elif owner == 0 and turns >= 2: # assign position each turn
            moved_self(x,y)
    print("MOVE 8 10")

    # My Debug Console
    """
    print("******************", file=sys.stderr)
    print("Entity_Type: ", entity_type, file=sys.stderr)
    print("Owner: ", owner, file=sys.stderr)
    print("Bomb Count : ", bombCount, file=sys.stderr)
    print("Blast Range : ", blastRange, file=sys.stderr)
    print("Turns : ", turns, file=sys.stderr)
    print("******************", file=sys.stderr)
    """

    # path_finder(startPos)
    # print("Path_Finder: ", path_finder(startPos), file=sys.stderr)
    # print("startPos Out: ", path_finder(*startPos), file=sys.stderr)





'''
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