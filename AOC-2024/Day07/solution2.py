from itertools import product

def concatenate_or_operate(a, b, operator):
    """Perform concatenation, addition, or multiplication."""
    if operator == "||":
        return int(str(a) + str(b))
    elif operator == "+":
        return a + b
    elif operator == "*":
        return a * b

def evaluate_equation(numbers, target):
    """Evaluate the equation using all operator combinations."""
    for ops in product(["+", "*", "||"], repeat=len(numbers) - 1):
        result = numbers[0]
        for i, op in enumerate(ops):
            result = concatenate_or_operate(result, numbers[i + 1], op)
        if result == target:
            return True
    return False

def calculate_total_calibration(file_path):
    """Parse the input file, evaluate equations, and return total calibration."""
    valid_calibration_total = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        try:
            target, num_str = line.strip().split(":")
            target = int(target)
            numbers = list(map(int, num_str.split()))
            if evaluate_equation(numbers, target):
                valid_calibration_total += target
        except ValueError:
            continue  # Skip lines with invalid formatting
    return valid_calibration_total

# Input file path
input_path = r"D:\CODING\iCode\Advent of code\AOC-2024\Day07\input2.txt"

# Calculate and print the total calibration result
result = calculate_total_calibration(input_path)
print("Total Calibration Result:", result)
