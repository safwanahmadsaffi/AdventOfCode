import sys
import re
from collections import *
from itertools import *
from heapq import *
import math
from rich import print

def count(it):
    return sum(1 for _ in it)

# Read the input from input.txt file
with open('D:\CODING\iCode\Advent of code\AOC-2024\Day15\input.txt', 'r') as file:
    inp = file.read()

parts = inp.split("\n\n")
lines = parts[0].split("\n")
m = len(lines)
n = len(lines[0])

# Build the grid from the input
grid = defaultdict(lambda: defaultdict(lambda: "!"), 
                  {i: defaultdict(lambda: "!", {j: line[j] for j in range(len(line))}) 
                   for i, line in enumerate(lines)})

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chardirs = {"<": 1, ">": 0, "^": 2, "v": 3}

result = 0

def move(d, i, j):
    if grid[i][j] == "#":
        return False
    elif grid[i][j] == ".":
        return True
    else:
        can_move = move(d, i + d[0], j + d[1])
        if can_move:
            grid[i + d[0]][j + d[1]] = grid[i][j]
            grid[i][j] = "."
            return True
        return False

robot_pos = (0, 0)
# Find the robot's initial position
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            robot_pos = (i, j)

# Process the directions from the second part of the input
for dirchar in parts[1]:
    if dirchar == "\n":
        continue
    d = dirs[chardirs[dirchar]]
    if move(d, robot_pos[0], robot_pos[1]):
        robot_pos = (robot_pos[0] + d[0], robot_pos[1] + d[1])

# Calculate the result based on the grid
for i in range(m):
    for j in range(n):
        if grid[i][j] == "O":
            result += 100 * i + j

# Print the final result
print(result)