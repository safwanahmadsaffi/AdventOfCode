def solve():
    with open("input.txt", "r") as f:
        content = f.read().strip()
    
    # Split by blank line
    parts = content.split("\n\n")
    ranges_part = parts[0]
    ingredients_part = parts[1]
    
    # Parse ranges
    ranges = []
    for line in ranges_part.split("\n"):
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    
    # Parse ingredient IDs
    ingredient_ids = [int(line) for line in ingredients_part.split("\n")]
    
    # Count fresh ingredients
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1
    
    print(f"Number of fresh ingredient IDs: {fresh_count}")
    return fresh_count

if __name__ == "__main__":
    solve()
