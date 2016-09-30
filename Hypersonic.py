import sys
width, height, my_id = [int(i) for i in input().split()]
turns = 0
startpos = False
beginpos = False
newPos = 0

# print("Lines: ",lines[1])
# assert ['bad width' for x in lines if len(x) != len(lines[0])] == [], "WORLD string needs to be rectangular."
def getWorldFromTextMap(textmap):
    # Converts the programmer-friendly version of a world typed out as ascii
    # characters in a multiline string into a source code-friendly version
    # that lets us access the map as world[x][y].
    worldWidth = int(12)
    worldHeight = int(10)

    textmap = textmap.strip().split('\n')

    world = []
    for i in range(worldWidth):
        world.append([''] * worldHeight)
    for x in range(worldWidth):
        for y in range(worldHeight):
            world[x][y] = textmap[y][x]
    return world

def printWorld(world):
    worldWidth = int(12)
    worldHeight = int(10)

    for y in range(worldHeight):
        for x in range(worldWidth):
            print(world[x][y], file=sys.stderr)

def floodFill(world, x, y, oldChar, newChar):
    # The recursive algorithm. Starting at x and y, changes any adjacent
    # characters that match oldChar to newChar.
    worldWidth = int(12)
    worldHeight = int(10)

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


def moved_self(x,y):
    beginpos = True
    new_x = x
    new_y = y
    if beginpos:
        beginpos = False
        print("MOVE", new_x, new_y)
    else:
        if x == 0 and y == 0:
            print("Move %d %d" % (x+2,y-2))
        if x == 12 and y == 0:
            print("Move %d %d" % (x-2,y)+2)

    #print("newPos Set: ", newPos, file=sys.stderr)
    print("MOVE %d %d" % (x,y))

def getSafe(x,y): # Check if character is in range and in danger, if yes MOVE to safety
    print("getSafe:", x, y, file=sys.stderr)
    if x >= 0 and y >= 10:
        print("GetSafe: 1", file=sys.stderr)
        print("MOVE %d %d" % (x+2, y-1))
    else:
        print("GetSafe: 2", file=sys.stderr)
        print("MOVE %d %d" % (x-1,y+2))
    print("BOMB", x, y)
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
    match = [(i, j) for i, row in enumerate(textmap) for j, cell in enumerate(row) if cell == '.']
    # print(match, file=sys.stderr)

    # Current loop game information
    entities = int(input())
    for i in range(entities):
        entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]
        if owner == 1 and entity_type == 1:
            # Detects if they dropped a bomb on the current tile
            getSafe(x,y)
            bombLocation = (x,y)
            print("bombLocation: ", bombLocation, file=sys.stderr)
        if owner == 0 and turns <= 1:  # ONLY on Turn 1 assign our starting position
            moved_self(x,y)
        elif owner == 0 and turns >= 2: # assign position each turn
            moved_self(x,y)

    def main():
        world = getWorldFromTextMap(textmap)
        print(printWorld(world), file=sys.stderr)

        floodFill(world, 5, 8, None, '+')
        print(printWorld(world), file=sys.stderr)

        floodFill(world, 0, 0, None, 's')
        print(printWorld(world), file=sys.stderr)

    if __name__ == '__main__':
        main()

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

    # path_finder(startpos)
    # print("Path_Finder: ", path_finder(startpos), file=sys.stderr)
    # print("startpos Out: ", path_finder(*startpos), file=sys.stderr)
