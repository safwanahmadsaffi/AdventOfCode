import os
from typing import List


def read_input_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


def is_invalid_id_part1(n: int) -> bool:
    """
    Part 1: Check if a number is made of some sequence of digits repeated exactly twice.
    e.g., 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(n)
    length = len(s)
    
    # Must have even length to be a repeated pattern
    if length % 2 != 0:
        return False
    
    half = length // 2
    # Check if first half equals second half
    return s[:half] == s[half:]


def is_invalid_id_part2(n: int) -> bool:
    """
    Part 2: Check if a number is made of some sequence of digits repeated at least twice.
    e.g., 1234 repeated 2 times, 123 repeated 3 times, 12 repeated 5 times, 1 repeated 7 times
    """
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    
    return False


def solve(input_path: str, part: int = 1) -> int:
    lines = read_input_lines(input_path)
    # Input is a single line with comma-separated ranges
    input_data = ''.join(line.strip() for line in lines)
    
    # Parse ranges
    ranges = input_data.split(',')
    
    is_invalid = is_invalid_id_part1 if part == 1 else is_invalid_id_part2
    
    total = 0
    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split('-'))
        
        # Find invalid IDs in this range
        for num in range(start, end + 1):
            if is_invalid(num):
                total += num
    
    return total


if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")
    result1 = solve(input_path, part=1)
    print(f"Part 1 - Sum of all invalid IDs: {result1}")
    
    result2 = solve(input_path, part=2)
    print(f"Part 2 - Sum of all invalid IDs: {result2}")
