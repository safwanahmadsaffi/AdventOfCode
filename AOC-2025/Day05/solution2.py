def solve_part2():
    with open("input.txt", "r") as f:
        content = f.read().strip()
    
    # Split by blank line
    parts = content.split("\n\n")
    ranges_part = parts[0]
    
    # Parse ranges
    ranges = []
    for line in ranges_part.split("\n"):
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    
    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    
    # Merge overlapping ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - extend the previous range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # No overlap - add new range
            merged.append((start, end))
    
    # Count total unique IDs
    total_fresh = 0
    for start, end in merged:
        total_fresh += end - start + 1
    
    print(f"Total fresh ingredient IDs: {total_fresh}")
    return total_fresh

if __name__ == "__main__":
    solve_part2()
