from collections import deque

# Load the input map
with open("input1.txt", "r") as f:
    lines = f.readlines()

# Parse the input into a 2D grid of integers
grid = [list(map(int, line.strip())) for line in lines]
rows, cols = len(grid), len(grid[0])

# Helper function to check if a position is within the grid bounds
def in_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

# Possible directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS to find reachable '9' positions from a given trailhead
def bfs_trailhead(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    reachable_nines = set()
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:  # Valid step (height increases by 1)
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if grid[nx][ny] == 9:  # Reached a height of 9
                        reachable_nines.add((nx, ny))
    
    return len(reachable_nines)

# Find all trailheads and calculate their scores
total_score = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:  # This is a trailhead
            total_score += bfs_trailhead(i, j)

# Output the total score
print("Total score of all trailheads:", total_score)
