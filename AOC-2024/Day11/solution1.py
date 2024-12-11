def split_stone(num):
    """Splits a stone into two parts if it has an even number of digits."""
    num_str = str(num)
    mid = len(num_str) // 2
    left = int(num_str[:mid])
    right = int(num_str[mid:])
    return [left, right]

def simulate_blinks(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.extend(split_stone(stone))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Initial stones
initial_stones = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]

# Simulate 25 blinks
result = simulate_blinks(initial_stones, 25)
print(f"Number of stones after 25 blinks: {result}")

