import sys
width, height, my_id = [int(i) for i in input().split()]
turns = 0  # TODO: Think of a better way to find out starting position on opening turn only
startPos = 0
# game loop
while True:
    turns += 1
    # print("Turn: ",turns, file=sys.stderr)
    grid = [[x for x in input()] for y in range(height)]  # a list of lists to show what is on the board
    entities = int(input())  # Current Players and Bomb Count on the board.
    for i in range(entities):
        entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]
        if owner == 0 and turns <= 1:  # ONLY on Turn 1 assign our starting position
            startPos = x,y
            print("Set Pos: ", startPos, file=sys.stderr)
        # My Debug Console
        """
        print("******************", file=sys.stderr)
        print("Entity_Type: ", entity_type, file=sys.stderr)
        print("Owner: ", owner, file=sys.stderr)
        print("X,Y : ", x, y, file=sys.stderr)
        print("Bomb Count : ", bombCount, file=sys.stderr)
        print("Blast Range : ", blastRange, file=sys.stderr)
        print("Turns : ", turns, file=sys.stderr)
        print("******************", file=sys.stderr)
        """
    def path_finder(x, y): # TODO: Let's determine the closest position to blow up the most boxes
        print("Grid XY: ", type(grid[x][y]), file=sys.stderr)
        # explore neighbors clockwise starting by the one on the right
        if ((x < len(grid) - 1 and path_finder(x + 1, y))
            or (y > 0 and path_finder(x, y - 1))
            or (x > 0 and path_finder(x - 1, y))
            or (y < len(grid) - 1 and path_finder(x, y + 1))):
            print("BOMB %d %d" % (x, y))
        else:
            newPos = x, y
            print("MOVE 9 10")

        return False
        # for i in board: # TODO: Compare each row to combo boxes within 3 spaces for max points
        #    for x in i:
    # path_finder(startPos)
    # print("Path_Finder: ", path_finder(startPos), file=sys.stderr)
    print("startPos Out: ", path_finder(*startPos), file=sys.stderr)
    print("MOVE 9 10")
