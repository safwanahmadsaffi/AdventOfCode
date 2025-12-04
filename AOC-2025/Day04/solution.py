def count_accessible_rolls(grid):
    """Part 1: Count rolls that can be accessed (fewer than 4 adjacent rolls)"""
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    accessible_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbor_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbor_count += 1
                
                if neighbor_count < 4:
                    accessible_count += 1
                    
    return accessible_count


def count_total_removable_rolls(grid):
    """Part 2: Count total rolls that can be removed by repeatedly removing accessible ones"""
    rows = len(grid)
    cols = len(grid[0])
    
    # Make a mutable copy
    grid = [list(row) for row in grid]
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    total_removed = 0
    
    while True:
        rolls_to_remove = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbor_count = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                neighbor_count += 1
                    
                    if neighbor_count < 4:
                        rolls_to_remove.append((r, c))
        
        if not rolls_to_remove:
            break
            
        for r, c in rolls_to_remove:
            grid[r][c] = '.'
            
        total_removed += len(rolls_to_remove)

    return total_removed


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines() if line.strip()]
    
    # Part 1
    part1 = count_accessible_rolls(grid)
    print(f"Part 1: {part1}")
    
    # Part 2
    part2 = count_total_removable_rolls(grid)
    print(f"Part 2: {part2}")
