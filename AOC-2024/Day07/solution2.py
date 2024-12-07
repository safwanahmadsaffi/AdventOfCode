from itertools import product

# Helper function to perform concatenation and other operations
def concatenate_or_operate(a, b, operator):
    if operator == "||":
        return int(str(a) + str(b))
    elif operator == "+":
        return a + b
    elif operator == "*":
        return a * b

# Function to evaluate an equation with all operator permutations
def evaluate_with_operators(numbers, target):
    for ops in product(["+", "*", "||"], repeat=len(numbers) - 1):
        result = numbers[0]
        for i, op in enumerate(ops):
            result = concatenate_or_operate(result, numbers[i + 1], op)
        if result == target:
            return True
    return False

# Load and parse the file content
file_path = '/mnt/data/input2.txt'
valid_calibration_total = 0

with open(file_path, 'r') as file:
    for line in file:
        # Parse target and numbers
        try:
            target, num_str = line.strip().split(":")
            target = int(target)
            numbers = list(map(int, num_str.split()))
            
            # Check if the equation is valid
            if evaluate_with_operators(numbers, target):
                valid_calibration_total += target
        except ValueError:
            continue

valid_calibration_total
