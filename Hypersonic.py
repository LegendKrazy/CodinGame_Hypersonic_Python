import sys
width, height, my_id = [int(i) for i in input().split()]
turns = 0  # TODO: Think of a better way to find out starting position on opening turn only
startPos = 0
beginPos = False
newPos = 0

def path_finder(x, y):  #TODO: Let's determine the closest position to blow up the most boxes
    #@TODO Pathfinder memes
    return x, y

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
while True:  # game loop for Bomberman clone contest: 400 turns and it ends
    turns += 1
    # print("Turn: ",turns, file=sys.stderr)
    grid = [[x for x in input()] for y in range(height)]  # a list of lists to show what is on the board
    # turn grid into coordinates
    match = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '.']
    print(match, file=sys.stderr)

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
