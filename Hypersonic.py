import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
width, height, my_id = [int(i) for i in input().split()]
board = [[x for x in input()] for y in range(height)]  # a list of lists to show what is on the board
turns = 0  # TODO: Think of a better way to find out starting position on opening turn only
# game loop
while True:
    turns += 1
    # print("Turn: ",turns, file=sys.stderr)
    entities = input() # Current Players and Bomb Count on the board.
    # print("Entities: " + str(entities), file=sys.stderr)
    for i in range(entities):
        entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]
        if turns == 1 and owner == 0:
            startPos = [x, y]
            print("startPos: ", startPos, file=sys.stderr)
        # Debug Console
        print("******************", file=sys.stderr)
        print("Entity_Type: " + str(entity_type), file=sys.stderr)
        print("Owner: " + str(owner), file=sys.stderr)
        print("X,Y : ", x, y, file=sys.stderr)
        print("Bomb Count : ", bombCount, file=sys.stderr)
        print("Blast Range : ", blastRange, file=sys.stderr)
        print("Turns : ", turns, file=sys.stderr)
        print("******************", file=sys.stderr)

    def path_finder(): # TODO: Let's determine the closest position to blow up the most boxes
        for i in board[x]: # TODO: Compare each row to combo boxes within 3 spaces for max points
            print("I: ", i, file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print("MOVE 9 10")
