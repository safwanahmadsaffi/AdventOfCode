from collections import defaultdict

# Read the input from the file
with open('input2.txt', 'r') as file:
    data = file.readlines()

# Parse the input into a grid
grid = [list(line.strip()) for line in data]

# Helper functions to parse positions and add coordinates
def add_positions(pos, dx, dy):
    return pos[0] + dx, pos[1] + dy

# Solution 1
def solution1(grid):
    antennas_by_char = defaultdict(list)
    anti_nodes = set()

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                antennas_by_char[char].append((x, y))

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                for eq_pos in antennas_by_char[char]:
                    if (x, y) == eq_pos:
                        continue
                    x_d, y_d = x - eq_pos[0], y - eq_pos[1]
                    anti_node_pos = add_positions((x, y), x_d, y_d)
                    if 0 <= anti_node_pos[0] < len(grid) and 0 <= anti_node_pos[1] < len(grid[0]):
                        anti_nodes.add(anti_node_pos)

    return len(anti_nodes)

# Solution 2
def solution2(grid):
    antennas_by_char = defaultdict(list)
    anti_nodes = set()

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                antennas_by_char[char].append((x, y))

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                for eq_pos in antennas_by_char[char]:
                    if (x, y) == eq_pos:
                        continue
                    x_d, y_d = x - eq_pos[0], y - eq_pos[1]
                    for p in [(x, y), eq_pos]:
                        anti_node_pos = add_positions(p, x_d, y_d)
                        while 0 <= anti_node_pos[0] < len(grid) and 0 <= anti_node_pos[1] < len(grid[0]):
                            anti_nodes.add(anti_node_pos)
                            anti_node_pos = add_positions(anti_node_pos, x_d, y_d)

    return len(anti_nodes)

# Calculate solutions
print("Solution 1:", solution1(grid))
print("Solution 2:", solution2(grid))
