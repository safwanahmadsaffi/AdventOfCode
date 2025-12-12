"""
Advent of Code 2025 - Day 12: Christmas Tree Farm
Present packing problem - fit shapes into regions using Dancing Links (DLX)
"""

import sys
from pathlib import Path

def parse_input(puzzle_input):
    """Parse shapes and regions from input."""
    lines = puzzle_input.strip().split('\n')
    
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        if line and line[0].isdigit() and ':' in line and 'x' not in line:
            idx = int(line.split(':')[0])
            shape_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() and ('x' not in lines[i] or ':' not in lines[i]):
                if lines[i].strip()[0].isdigit() and ':' in lines[i].strip():
                    break
                shape_lines.append(lines[i])
                i += 1
            
            shape = []
            for sl in shape_lines:
                row = [1 if ch == '#' else 0 for ch in sl]
                shape.append(row)
            shapes[idx] = shape
        
        elif 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip()
            width, height = map(int, dims.split('x'))
            counts = list(map(int, parts[1].strip().split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions


def get_shape_cells(shape):
    """Get list of (row, col) cells that are part of the shape."""
    cells = []
    for r, row in enumerate(shape):
        for c, val in enumerate(row):
            if val == 1:
                cells.append((r, c))
    return cells


def rotate_90(cells):
    """Rotate cells 90 degrees clockwise."""
    return [(c, -r) for r, c in cells]


def flip_horizontal(cells):
    """Flip cells horizontally."""
    return [(r, -c) for r, c in cells]


def normalize(cells):
    """Normalize cells to start at (0, 0)."""
    if not cells:
        return tuple()
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    return tuple(sorted((r - min_r, c - min_c) for r, c in cells))


def get_all_orientations(shape):
    """Get all unique orientations (rotations and flips) of a shape."""
    cells = get_shape_cells(shape)
    orientations = set()
    
    current = cells
    for _ in range(4):
        orientations.add(normalize(current))
        orientations.add(normalize(flip_horizontal(current)))
        current = rotate_90(current)
    
    return [list(o) for o in orientations]


# Dancing Links implementation
class DLXNode:
    __slots__ = ['left', 'right', 'up', 'down', 'column', 'row_id']
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = -1

class DLXColumn(DLXNode):
    __slots__ = ['size', 'name']
    def __init__(self, name):
        super().__init__()
        self.size = 0
        self.name = name
        self.column = self


class DLX:
    def __init__(self, num_cols, primary_cols):
        self.header = DLXColumn("header")
        self.columns = []
        self.solution = []
        self.primary_cols = primary_cols
        
        prev = self.header
        for i in range(num_cols):
            col = DLXColumn(i)
            self.columns.append(col)
            if i < primary_cols:
                col.left = prev
                col.right = self.header
                prev.right = col
                self.header.left = col
                prev = col
    
    def add_row(self, row_id, cols):
        if not cols:
            return
        first = None
        prev = None
        for c in cols:
            col = self.columns[c]
            node = DLXNode()
            node.row_id = row_id
            node.column = col
            
            node.down = col
            node.up = col.up
            col.up.down = node
            col.up = node
            col.size += 1
            
            if first is None:
                first = node
                prev = node
            else:
                node.left = prev
                node.right = first
                prev.right = node
                first.left = node
                prev = node
    
    def cover(self, col):
        col.right.left = col.left
        col.left.right = col.right
        row = col.down
        while row != col:
            node = row.right
            while node != row:
                node.down.up = node.up
                node.up.down = node.down
                node.column.size -= 1
                node = node.right
            row = row.down
    
    def uncover(self, col):
        row = col.up
        while row != col:
            node = row.left
            while node != row:
                node.column.size += 1
                node.down.up = node
                node.up.down = node
                node = node.left
            row = row.up
        col.right.left = col
        col.left.right = col
    
    def search(self):
        if self.header.right == self.header:
            return True
        
        # Choose column with minimum size (MRV heuristic)
        min_size = float('inf')
        chosen = None
        col = self.header.right
        while col != self.header:
            if col.size < min_size:
                min_size = col.size
                chosen = col
            col = col.right
        
        if chosen is None or chosen.size == 0:
            return False
        
        self.cover(chosen)
        
        row = chosen.down
        while row != chosen:
            self.solution.append(row.row_id)
            
            node = row.right
            while node != row:
                self.cover(node.column)
                node = node.right
            
            if self.search():
                return True
            
            self.solution.pop()
            
            node = row.left
            while node != row:
                self.uncover(node.column)
                node = node.left
            
            row = row.down
        
        self.uncover(chosen)
        return False


def solve_region(width, height, shapes, counts):
    """Solve using backtracking - presents don't need to fill exactly."""
    # Build pieces list
    pieces = []
    for shape_idx, count in enumerate(counts):
        if shape_idx in shapes and count > 0:
            orientations = get_all_orientations(shapes[shape_idx])
            size = len(get_shape_cells(shapes[shape_idx]))
            for _ in range(count):
                pieces.append((size, orientations))
    
    if not pieces:
        return True
    
    # Calculate total cells needed
    total_cells = sum(size for size, _ in pieces)
    if total_cells > width * height:
        return False
    
    # Sort by size (larger first) for better pruning
    pieces.sort(key=lambda x: -x[0])
    pieces = [orientations for _, orientations in pieces]
    
    grid = [[0] * width for _ in range(height)]
    
    def can_place(cells, start_r, start_c):
        for dr, dc in cells:
            r, c = start_r + dr, start_c + dc
            if r < 0 or r >= height or c < 0 or c >= width:
                return False
            if grid[r][c] != 0:
                return False
        return True
    
    def place(cells, start_r, start_c, value):
        for dr, dc in cells:
            grid[start_r + dr][start_c + dc] = value
    
    def remove(cells, start_r, start_c):
        for dr, dc in cells:
            grid[start_r + dr][start_c + dc] = 0
    
    def backtrack(piece_idx):
        if piece_idx == len(pieces):
            return True
        
        # Try all positions for this piece
        for cells in pieces[piece_idx]:
            max_r = max(r for r, c in cells) if cells else 0
            max_c = max(c for r, c in cells) if cells else 0
            
            for start_r in range(height - max_r):
                for start_c in range(width - max_c):
                    if can_place(cells, start_r, start_c):
                        place(cells, start_r, start_c, piece_idx + 1)
                        if backtrack(piece_idx + 1):
                            return True
                        remove(cells, start_r, start_c)
        
        return False
    
    return backtrack(0)


def solve_region_backtrack(width, height, shapes, counts):
    """Backtracking solver for non-exact fills."""
    pieces = []
    for shape_idx, count in enumerate(counts):
        if shape_idx in shapes:
            orientations = get_all_orientations(shapes[shape_idx])
            size = len(get_shape_cells(shapes[shape_idx]))
            for _ in range(count):
                pieces.append((size, orientations))
    
    if not pieces:
        return True
    
    total_cells_needed = sum(size for size, _ in pieces)
    if total_cells_needed > width * height:
        return False
    
    pieces.sort(key=lambda x: -x[0])
    pieces = [orientations for _, orientations in pieces]
    
    grid = [[0] * width for _ in range(height)]
    
    def find_first_empty():
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 0:
                    return (r, c)
        return None
    
    def can_place(cells, start_r, start_c):
        for dr, dc in cells:
            r, c = start_r + dr, start_c + dc
            if r < 0 or r >= height or c < 0 or c >= width:
                return False
            if grid[r][c] != 0:
                return False
        return True
    
    def place(cells, start_r, start_c, value):
        for dr, dc in cells:
            grid[start_r + dr][start_c + dc] = value
    
    def remove(cells, start_r, start_c):
        for dr, dc in cells:
            grid[start_r + dr][start_c + dc] = 0
    
    def backtrack(piece_idx):
        if piece_idx == len(pieces):
            return True
        
        first_empty = find_first_empty()
        if first_empty is None:
            return piece_idx == len(pieces)
        
        er, ec = first_empty
        
        for cells in pieces[piece_idx]:
            for dr, dc in cells:
                start_r, start_c = er - dr, ec - dc
                if start_r < 0 or start_c < 0:
                    continue
                
                max_r = max(r for r, c in cells)
                max_c = max(c for r, c in cells)
                
                if start_r + max_r >= height or start_c + max_c >= width:
                    continue
                
                if can_place(cells, start_r, start_c):
                    place(cells, start_r, start_c, piece_idx + 1)
                    if backtrack(piece_idx + 1):
                        return True
                    remove(cells, start_r, start_c)
        
        return False
    
    return backtrack(0)


def solve_part1(shapes, regions):
    """Count how many regions can fit all their presents."""
    count = 0
    for i, (width, height, shape_counts) in enumerate(regions):
        print(f"Region {i+1}/{len(regions)}: {width}x{height}...", end=" ", flush=True)
        if solve_region(width, height, shapes, shape_counts):
            print("YES")
            count += 1
        else:
            print("NO")
    return count


def read_input(filename="input.txt"):
    """Read puzzle input from file."""
    script_dir = Path(__file__).parent
    input_path = script_dir / filename
    
    try:
        with open(input_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find '{input_path}'")
        sys.exit(1)


def main():
    puzzle_input = read_input("input.txt")
    shapes, regions = parse_input(puzzle_input)
    
    print(f"Loaded {len(shapes)} shapes and {len(regions)} regions\n")
    
    result = solve_part1(shapes, regions)
    print(f"\nPart 1: {result}")


if __name__ == "__main__":
    main()
