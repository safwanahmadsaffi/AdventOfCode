import os
from typing import List

def read_input_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def max_joltage(bank: str, num_digits: int = 2) -> int:
    """Find the maximum joltage from a bank by selecting num_digits batteries."""
    bank = bank.strip()
    n = len(bank)
    
    # Greedy approach: at each step, pick the largest digit possible
    # while ensuring enough digits remain to complete the selection
    result = []
    start = 0
    
    for remaining in range(num_digits, 0, -1):
        # We need to pick 'remaining' more digits
        # The latest position we can pick from is n - remaining
        end = n - remaining + 1
        
        # Find the maximum digit in the range [start, end)
        max_digit = '0'
        max_pos = start
        for i in range(start, end):
            if bank[i] > max_digit:
                max_digit = bank[i]
                max_pos = i
        
        result.append(max_digit)
        start = max_pos + 1
    
    return int(''.join(result))

def solve(lines: List[str], num_digits: int = 2) -> int:
    """Calculate total output joltage."""
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            total += max_joltage(line, num_digits)
    return total

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = read_input_lines(input_path)
    
    # Part 1
    result1 = solve(lines, 2)
    print(f"Part 1 - Total output joltage: {result1}")
    
    # Part 2
    result2 = solve(lines, 12)
    print(f"Part 2 - Total output joltage: {result2}")
