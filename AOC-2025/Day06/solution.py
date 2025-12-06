def solve():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    # Remove newline characters but keep the lines as-is (preserve spacing)
    lines = [line.rstrip('\n') for line in lines]
    
    # Make all lines the same length by padding with spaces
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    
    # Find separator columns - columns where ALL rows have a space
    separator_cols = set()
    for col in range(max_len):
        if all(line[col] == ' ' for line in lines):
            separator_cols.add(col)
    
    # Group consecutive non-separator columns into problems
    problems = []
    col = 0
    while col < max_len:
        # Skip separator columns
        if col in separator_cols:
            col += 1
            continue
        
        # Found start of a problem - find where it ends
        start_col = col
        while col < max_len and col not in separator_cols:
            col += 1
        end_col = col
        
        # Extract the numbers from each row (except last) for this column range
        numbers = []
        for row in lines[:-1]:
            num_str = row[start_col:end_col].strip()
            if num_str:
                numbers.append(int(num_str))
        
        # Get the operation from the last line
        op = lines[-1][start_col:end_col].strip()
        
        if numbers and op:
            problems.append((numbers, op))
    
    # Solve each problem (Part 1)
    total = 0
    for numbers, op in problems:
        if op == '+':
            result = sum(numbers)
        elif op == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operation: {op}")
        total += result
    
    print(f"Part 1 - Number of problems: {len(problems)}")
    print(f"Part 1 - Grand total: {total}")
    
    # Part 2: Each column within a problem represents one NUMBER
    # The digits of that number are stacked vertically (top = most significant)
    # Read columns right-to-left to get the numbers in order
    
    problems_p2 = []
    col = 0
    while col < max_len:
        # Skip separator columns
        if col in separator_cols:
            col += 1
            continue
        
        # Found start of a problem - find where it ends
        start_col = col
        while col < max_len and col not in separator_cols:
            col += 1
        end_col = col
        
        # Get the operation from the last line
        op = lines[-1][start_col:end_col].strip()
        
        num_rows = len(lines) - 1  # Exclude operation row
        
        # Each column within this problem gives one number
        # Read columns from RIGHT to LEFT
        numbers = []
        for c in range(end_col - 1, start_col - 1, -1):
            # Build the number from this column (top to bottom = most to least significant)
            digits = ''
            for row_idx in range(num_rows):
                char = lines[row_idx][c]
                if char.isdigit():
                    digits += char
            if digits:
                numbers.append(int(digits))
        
        if numbers and op:
            problems_p2.append((numbers, op))
    
    # Solve each problem (Part 2)
    total_p2 = 0
    for numbers, op in problems_p2:
        if op == '+':
            result = sum(numbers)
        elif op == '*':
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operation: {op}")
        total_p2 += result
    
    print(f"\nPart 2 - Number of problems: {len(problems_p2)}")
    print(f"Part 2 - Grand total: {total_p2}")
    
    return total, total_p2

if __name__ == "__main__":
    solve()
