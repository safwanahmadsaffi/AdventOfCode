def solve_part1(filename):
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find the starting position 'S'
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break
    
    # Track active beams - each beam is a column position
    # Beams move downward row by row
    # Use a set to track unique beam positions (column) at each row
    active_beams = {start_col}
    split_count = 0
    
    # Process row by row starting from row 1 (below S)
    for row in range(1, rows):
        new_beams = set()
        
        for col in active_beams:
            if 0 <= col < cols:
                cell = grid[row][col]
                if cell == '^':
                    # Beam hits a splitter - count the split and create two new beams
                    split_count += 1
                    # Left beam
                    if col - 1 >= 0:
                        new_beams.add(col - 1)
                    # Right beam
                    if col + 1 < cols:
                        new_beams.add(col + 1)
                elif cell == '.' or cell == 'S':
                    # Beam continues through empty space
                    new_beams.add(col)
                # If beam goes out of bounds or hits something else, it stops
        
        active_beams = new_beams
        
        # If no more beams, we're done
        if not active_beams:
            break
    
    return split_count


def solve_part2(filename):
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find the starting position 'S'
    start_col = None
    for c in range(cols):
        if grid[0][c] == 'S':
            start_col = c
            break
    
    # Track timelines at each column position
    # Key: column, Value: number of timelines at that position
    from collections import defaultdict
    timelines = defaultdict(int)
    timelines[start_col] = 1  # Start with 1 timeline
    
    # Process row by row starting from row 1 (below S)
    for row in range(1, rows):
        new_timelines = defaultdict(int)
        
        for col, count in timelines.items():
            if 0 <= col < cols:
                cell = grid[row][col]
                if cell == '^':
                    # Each timeline splits into two: one goes left, one goes right
                    if col - 1 >= 0:
                        new_timelines[col - 1] += count
                    if col + 1 < cols:
                        new_timelines[col + 1] += count
                elif cell == '.' or cell == 'S':
                    # Timeline continues through empty space
                    new_timelines[col] += count
                # If timeline goes out of bounds, it ends (but still counts as a timeline)
        
        timelines = new_timelines
        
        # If no more active timelines, we're done
        if not timelines:
            break
    
    # Sum up all timelines that made it through (or ended at bottom)
    return sum(timelines.values())


if __name__ == "__main__":
    result1 = solve_part1("input.txt")
    print(f"Part 1: {result1}")
    
    result2 = solve_part2("input.txt")
    print(f"Part 2: {result2}")
