'''
Chapter 4 Character Picture Grid

Basically take this grid below and print it so the image is shifted 90 degrees
to the right

You will need to use a loop in a loop in order to print grid[0][0],
then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
This will finish the first row, so then print a newline.
Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
The last thing your program will print is grid[8][5].
'''
from time import sleep

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for x in range(len(grid[0])):
    print()
    for y in range(len(grid)-1,-1,-1):
        print(grid[y][x],end=' ')
        sleep(0.2) #added sleep to display the image being drawn
print()
print()