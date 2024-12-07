from itertools import product

# Define the input file path
input_file_path = 'D:/CODING/iCode/Advent of code/AOC-2024/Day07/input1.txt'

# Helper function to evaluate expressions left-to-right
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
    return result

# Function to process the input and calculate the result
def calculate_total_calibration(input_file_path):
    # Read the entire file at once
    with open(input_file_path, "r") as file:
        lines = file.readlines()
    
    total_calibration_result = 0

    # Process each line
    for line in lines:
        target_value, numbers_str = line.strip().split(":")
        target_value = int(target_value)
        numbers = list(map(int, numbers_str.split()))
        
        # Generate operator combinations and evaluate
        num_ops = len(numbers) - 1
        valid = any(
            evaluate_expression(numbers, operators) == target_value
            for operators in product(["+", "*"], repeat=num_ops)
        )
        
        # Add to the total if valid
        if valid:
            total_calibration_result += target_value
    
    return total_calibration_result

# Calculate and print the result
result = calculate_total_calibration(input_file_path)
print(f"Total calibration result: {result}")
