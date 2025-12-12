"""
Advent of Code 2025 - Day XX
Template for solving AoC puzzles
"""

import sys
from pathlib import Path
from collections import defaultdict, deque, Counter
from functools import lru_cache
import re

# ============================================================================
# INPUT PARSING
# ============================================================================

def parse_input(puzzle_input):
    """
    Parse the raw puzzle input into a usable data structure.
    
    Common patterns:
    - Lines: puzzle_input.strip().split('\n')
    - Grid: [list(line) for line in puzzle_input.strip().split('\n')]
    - Numbers: [int(x) for x in puzzle_input.strip().split('\n')]
    - CSV: [int(x) for x in puzzle_input.strip().split(',')]
    - Blocks: puzzle_input.strip().split('\n\n')
    """
    lines = [line.strip() for line in puzzle_input.strip().split('\n') if line.strip()]
    return lines

def parse_grid(puzzle_input):
    """Parse input as a 2D grid."""
    return [list(line) for line in puzzle_input.strip().split('\n')]

def parse_numbers(puzzle_input):
    """Parse input as a list of numbers (one per line)."""
    return [int(line) for line in puzzle_input.strip().split('\n') if line.strip()]

def parse_graph(puzzle_input):
    """Parse input as an adjacency list graph."""
    graph = defaultdict(list)
    lines = [line.strip() for line in puzzle_input.strip().split('\n') if line.strip()]
    
    for line in lines:
        # Adjust parsing based on input format
        # Example: "node: neighbor1 neighbor2 neighbor3"
        parts = line.split(':')
        source = parts[0].strip()
        if len(parts) > 1:
            destinations = parts[1].strip().split()
            graph[source] = destinations
        else:
            graph[source] = []
    
    return graph

# ============================================================================
# SOLUTION FUNCTIONS
# ============================================================================

def solve_part1(data):
    """
    Solve Part 1 of the puzzle.
    """
    result = 0
    
    # TODO: Implement Part 1 solution
    for item in data:
        pass  # Your logic here
    
    return result

def solve_part2(data):
    """
    Solve Part 2 of the puzzle.
    """
    result = 0
    
    # TODO: Implement Part 2 solution
    for item in data:
        pass  # Your logic here
    
    return result

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def bfs(graph, start, end):
    """Breadth-First Search - finds shortest path."""
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return -1  # No path found

def dfs_count_paths(graph, start, end, memo=None):
    """DFS with memoization - counts all paths from start to end."""
    if memo is None:
        memo = {}
    
    if start == end:
        return 1
    
    if start not in graph:
        return 0
    
    if start in memo:
        return memo[start]
    
    total = 0
    for neighbor in graph[start]:
        total += dfs_count_paths(graph, neighbor, end, memo)
    
    memo[start] = total
    return total

def get_neighbors_4(row, col, max_row, max_col):
    """Get 4-directional neighbors (up, down, left, right)."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < max_row and 0 <= nc < max_col:
            neighbors.append((nr, nc))
    return neighbors

def get_neighbors_8(row, col, max_row, max_col):
    """Get 8-directional neighbors (including diagonals)."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < max_row and 0 <= nc < max_col:
                neighbors.append((nr, nc))
    return neighbors

# ============================================================================
# FILE I/O
# ============================================================================

def read_input(filename="input.txt"):
    """Read puzzle input from a file."""
    script_dir = Path(__file__).parent
    input_path = script_dir / filename
    
    try:
        with open(input_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find '{input_path}'")
        sys.exit(1)

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point."""
    # Read input from file
    puzzle_input = read_input("input.txt")
    
    # Parse the input (choose appropriate parser)
    data = parse_input(puzzle_input)
    # data = parse_grid(puzzle_input)
    # data = parse_numbers(puzzle_input)
    # data = parse_graph(puzzle_input)
    
    # Solve and print results
    part1_result = solve_part1(data)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part2(data)
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
