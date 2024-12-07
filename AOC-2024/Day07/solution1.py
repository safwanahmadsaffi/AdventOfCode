from itertools import product

# Load the input file
input_file_path = 'D:\CODING\iCode\Advent of code\AOC-2024\Day07\input1.txt'

# Parse the input
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Process each line into a target and numbers
data = []
for line in lines:
    target, numbers = line.split(":")
    target = int(target.strip())
    numbers = list(map(int, numbers.split()))
    data.append((target, numbers))

# Function to evaluate all combinations of operators
def evaluate_combinations(target, numbers):
    if len(numbers) == 1:
        return numbers[0] == target
    
    # Possible operators: +, *
    operators = ['+', '*']
    for ops in product(operators, repeat=len(numbers) - 1):
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            if result > target:  # Early termination if result exceeds target
                break
        if result == target:
            return True
    return False

# Evaluate each equation and calculate the total calibration result
valid_targets = []
for target, numbers in data:
    if evaluate_combinations(target, numbers):
        valid_targets.append(target)

# Calculate the total calibration result
total_calibration_result = sum(valid_targets)
total_calibration_result
