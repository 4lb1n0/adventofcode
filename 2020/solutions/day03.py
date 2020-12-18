# --- Day 3: Toboggan Trajectory ---
''' Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. (day03.txt)
The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:
From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.'''

# --- PART 01 ---
# How many trees did you encounter?

file = open("day03.txt")
lines = file.read().split("\n") # we get list of lists for our path

x = 0
y = 0
trees = 0

for i in lines:
    if lines[y][x % len(lines[0])] == "#":
        trees += 1
    x += 3
    y += 1

print(trees) # 159 in our case

# --- PART 02 ---

''' Determine the number of trees you would encounter if, for each of the following slopes, 
you start at the top-left corner and traverse the map all the way to the bottom'''

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

file = open("input.txt")
lines = file.read().split("\n")

# I added the function so I don't have to manually check for each slope
def check_trees(right, down, path):
    x = 0
    y = 0
    trees = 0
    # Had to change from for command to while command because in the last slope we get down = 2, which in this case goes beyond all the rows
    # We get index out of range error
    while y < len(path):
        if path[y][x % len(path[0])] == "#":
            trees += 1
        x += right
        y += down
    return trees

final_multiplier = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for slope in slopes:
    final_multiplier *= check_trees(slope[0], slope[1], lines)

print(final_multiplier) # 6419669520
