# MineSweeper
Created in November 2021. My implementation of MineSweeper.

Run the file to play the game.

This game took about 3 hours to create, and it is definitely not perfect. 
The amount of tiles, mines, percent of bombs on the map, can all be changed as they are variables, through the python file.

I used a recursive algorithm to open tiles which had no bombs in the surrounding tiles, and then it opens the tiles around itself which also doesnt have bombs in the surrounding tiles. Which was somewhat difficult to implement considering the corner pieces had less than 8 surrounding tiles.

Another interesting feature is when you right click, it puts a "flag" on the tile, so the tile cannot be opened, regardless of whether there is a bomb there or not, a second right click will undo this "flag".

DISCLAIMER: the game doesn't end when you "lose", when you accidently open a tile with a bomb.
