import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height, my_id = [int(i) for i in input().split()]

turns = 0
# game loop
while True:
    turns += 1
    print("Turn: ",turns, file=sys.stderr)

    for i in range(height):
        row = input()  # Line by line grid, output . is empty space, 0 is a box
        # print("Row: " + row, file=sys.stderr)
    entities = int(input()) # Players and Bomb Count
    # print("Entities: " + str(entities), file=sys.stderr)
    for i in range(entities):
        entity_type, owner, x, y, bombCount, blastRange = [int(j) for j in input().split()]
        print("Entity_Type: " + str(entity_type), file=sys.stderr)
        print("X,Y : ", x, y, file=sys.stderr)
        print("Bomb Count : ", bombCount, file=sys.stderr)
        print("Blast Range : ", blastRange, file=sys.stderr)
        print("Turns : ", turns, file=sys.stderr)
    # Let's determine the closest position to blow up the most boxes
    def path_finder():
        print("TEST")
        # placeholder


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("BOMB 6 5")
