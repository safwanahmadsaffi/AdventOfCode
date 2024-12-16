from rich import print

def parse_input(data):
    robots = []
    for line in data:
        p, v = line.strip().split(' ')
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robot(position, velocity, width, height):
    x, y = position
    vx, vy = velocity
    x = (x + vx) % width
    y = (y + vy) % height
    return (x, y)

def simulate_robots(robots, width, height, seconds):
    for _ in range(seconds):
        robots = [(move_robot(p, v, width, height), v) for p, v in robots]
    return robots

def count_robots_in_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]
    for (x, y), _ in robots:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1
    return quadrants

def check_christmas_tree_pattern(robots, width, height):
    tree_pattern = [
        "....#....",
        "...###...",
        "..#####..",
        ".#######.",
        "#########",
        "....#....",
        "....#...."
    ]

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y), _ in robots:
        grid[y][x] = '#'

    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])

    for y in range(height - pattern_height + 1):
        for x in range(width - pattern_width + 1):
            match = True
            for py in range(pattern_height):
                for px in range(pattern_width):
                    if tree_pattern[py][px] == '#' and grid[y + py][x + px] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def find_easter_egg(data):
    width, height = 101, 103
    robots = parse_input(data)
    seconds = 0
    while True:
        robots = simulate_robots(robots, width, height, 1)
        seconds += 1
        if check_christmas_tree_pattern(robots, width, height):
            return seconds

def solve(data):
    width, height = 101, 103
    robots = parse_input(data)
    robots = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(robots, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

def main():
    # Update this to the path of your input file
    file_path = 'D:\CODING\iCode\Advent of code\AOC-2024\Day14\input.txt'

    # Read the input data from the file
    with open(file_path, 'r') as file:
        data = file.readlines()

    print("Safety Factor:", solve(data))
    print("Seconds to Easter Egg:", find_easter_egg(data))

if __name__ == '__main__':
    main()