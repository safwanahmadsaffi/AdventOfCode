def solve():
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines() if line.strip()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    def count_adjacent_rolls(r, c):
        """Count adjacent rolls of paper"""
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < len(grid[nr]) and grid[nr][nc] == '@':
                count += 1
        return count
    
    def find_accessible():
        """Find all rolls that can be accessed (fewer than 4 adjacent rolls)"""
        accessible = []
        for r in range(rows):
            for c in range(len(grid[r])):
                if grid[r][c] == '@' and count_adjacent_rolls(r, c) < 4:
                    accessible.append((r, c))
        return accessible
    
    total_removed = 0
    
    while True:
        accessible = find_accessible()
        if not accessible:
            break
        
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    print(total_removed)

if __name__ == "__main__":
    solve()
