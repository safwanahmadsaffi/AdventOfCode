 # Read the input data
with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")

# Initialize variables
part1 = part2 = 0
l1, l2 = [], []

# Process input into two separate lists
for line in data:
    a, b = map(int, line.split())  # Split by whitespace (space or tab)
    l1.append(a)
    l2.append(b)

# Sort both lists for Part 1
l1.sort()
l2.sort()

# Part 1 calculation: Manhattan distance
for ix in range(len(l1)):
    part1 += abs(l1[ix] - l2[ix])

# Part 2 calculation: Product-based matching
for value in l1:
    part2 += value * l2.count(value)

# Print results
print("Part 1:", part1)
print("Part 2:", part2)
