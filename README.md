# CodinGame_Hypersonic_Python
CodinGame September 2016 Contest attempt in Python

The Goal:

Destroy more boxes than your opponent with your bombs in this Bomberman-inspired game.
 	Rules

The game is played on a grid 13 units wide and 11 units high. The coordinate X=0, Y=0 is the top left cell.

For now, the game is played with 2 players only. Each player starts out on a corner of the map.
All actions players take are computed simultaneously.

Boxes are scattered across the grid, and can be destroyed by bombs.

The map works as follows:
Each cell of the grid is either a floor or a box. Floor cells are indicated by a dot (.), and boxes by a zero (0).
Floor cells may be occupied by any number of players.
A random amount of boxes between 30 and 65 inclusive will be placed symmetrically across the grid.
The players work as follows:
Every turn, a player may move horizontally or vertically to an adjacent floor cell. If a bomb is already occupying that cell, the player won't be able to move there.
Players can occupy the same cell as a bomb only when the bomb appears on the same turn as when the player enters the cell.
Using the MOVE command followed by grid coordinates will make the player attempt to move one cell closer to those coordinates. The player will automatically compute the shortest path within the grid to get to the target point. If the given coordinates are impossible to get to, the player will instead target the valid cell closest to the given coordinates.
Using the BOMB command followed by map coordinates will make the player attempt to place a bomb on the currently occupied cell, then move one cell closer to the given coordinates.
Players may stay on the cell on which they place a bomb.
Players can only have 1 bomb in the grid at one time.
In this league, players are not hurt by bombs (they are using practice explosives).
The bombs work as follows:
Bombs have an 8 round timer. On each subsequent round, the timer will decrease by 1. On the round where the timers hits 0, the bomb explodes.
In this league, explosions have a range of 3, meaning they span horizontally and vertically up to 3 squares in each direction unless they encounter a box or other bomb.
Explosions will cause the boxes they hit to be destroyed.
Explosions will cause the bombs they hit to also explode.
After 200 rounds, the player who hit the most boxes with their bombs wins.

The game state of every round is given to you as a list of entities, each with a entityType, owner, position, param1 and param2.

The entityType will be:
For players: 0.
For bombs: 1.
The owner will be:
For players: id of the player (0 or 1).
For bombs: id of the bomb's owner.
The param1 will be:
For players: number of bombs the player can still place.
For bombs: number of rounds left until the bomb explodes.
The param2 is not useful for the current league, and will always be:
For players: explosion range of the player's bombs (=3).
For bombs: explosion range of the bomb (=3).

*****************************************************************
Victory Conditions
You are the one who blew up the most boxes.
 
Lose Conditions
Your program does not respond in time.
You provide invalid input.
