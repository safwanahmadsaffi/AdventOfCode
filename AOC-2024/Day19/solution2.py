from collections import defaultdict
import os
from rich import print

def count_ways_to_form_design(patterns, design):
    """
    Function to count the number of ways a design can be formed using the given patterns.
    """
    pattern_set = set(patterns)

    # Dynamic Programming to count the number of ways to form the design
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Base case: one way to form an empty design

    for i in range(1, len(design) + 1):
        for j in range(i):
            if design[j:i] in pattern_set:
                dp[i] += dp[j]

    return dp[len(design)]

# File path to the input file
file_path = "input.txt"

# Read input from the file
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")
else:
    raise FileNotFoundError(f"File not found at {file_path}")

# Parse the input
patterns = lines[0].split(", ")

# Separate the designs
if "" in lines:
    designs_index = lines.index("") + 1
else:
    raise ValueError("Input format error: Missing blank line separating patterns and designs.")

designs = lines[designs_index:]

# Calculate the total number of ways to form all designs
total_ways = 0

for design in designs:
    total_ways += count_ways_to_form_design(patterns, design)

# Output the result
print(f"Total number of ways to form all designs: {total_ways}")