from collections import deque

def simulate_falling_bytes(grid_size, corrupted_coords, max_bytes):
    # Initialize the grid
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    # Mark corrupted positions in the grid
    for x, y in corrupted_coords[:max_bytes]:
        grid[y][x] = "#"

    return grid

def find_shortest_path(grid):
    grid_size = len(grid)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    # BFS initialization
    queue = deque([(start, 0)])  # (current_position, steps)
    visited = set()
    visited.add(start)

    # BFS loop
    while queue:
        (x, y), steps = queue.popleft()

        # Check if we've reached the end
        if (x, y) == end:
            return steps

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # Check bounds and validity
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == ".":
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    # If no path found
    return -1

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    corrupted_coords = [tuple(map(int, line.strip().split(','))) for line in lines]
    return corrupted_coords

# Main execution
if __name__ == "__main__":
    input_file = "input.txt"
    corrupted_coords = read_input(input_file)

    grid_size = 71  # Actual grid size
    max_bytes = 1024  # Simulate first 1024 bytes

    # Simulate falling bytes
    grid = simulate_falling_bytes(grid_size, corrupted_coords, max_bytes)

    # Find the shortest path
    shortest_path = find_shortest_path(grid)

    # Print results
    print("Grid after falling bytes:")
    for row in grid:
        print("".join(row))

    print(f"Shortest path length: {shortest_path}")