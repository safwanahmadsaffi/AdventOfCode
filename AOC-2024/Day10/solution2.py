from collections import deque

# Load the input map
with open("/mnt/data/input1.txt", "r") as f:
    lines = f.readlines()

# Parse the input into a 2D grid of integers
grid = [list(map(int, line.strip())) for line in lines]
rows, cols = len(grid), len(grid[0])

# Helper function to check if a position is within bounds
def in_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

# Possible directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS to explore all distinct trails starting at a trailhead
def count_trails(x, y):
    # Stack-based DFS to track each path and visited nodes in the current path
    stack = [(x, y, set())]  # (current_x, current_y, path_visited)
    trail_count = 0
    
    while stack:
        cx, cy, visited = stack.pop()
        visited.add((cx, cy))
        
        # If the current height is 9, we've found a valid trail
        if grid[cx][cy] == 9:
            trail_count += 1
            continue
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == grid[cx][cy] + 1:
                stack.append((nx, ny, visited.copy()))
    
    return trail_count

# Calculate the total rating for all trailheads
total_rating = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:  # This is a trailhead
            total_rating += count_trails(i, j)

# Output the total rating
print("Total rating of all trailheads:", total_rating)
