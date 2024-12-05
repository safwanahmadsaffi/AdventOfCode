
# Function to solve the corrupted memory problem
def solve_corrupted_memory(corrupted_memory):
    # Define a regular expression pattern to match 'mul(X,Y)' where X and Y are integers
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches for the 'mul(X,Y)' pattern
    matches = re.findall(pattern, corrupted_memory)
    
    # Initialize the total sum
    total_sum = 0
    
    # For each match, parse the two numbers, multiply them, and add the result to the total
    for match in matches:
        x = int(match[0])  # Convert first number (X) to an integer
        y = int(match[1])  # Convert second number (Y) to an integer
        total_sum += x * y
    
    return total_sum

# Function to read input from a file
def read_input_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read the entire content of the file
            return file.read().strip()  # Read all text and remove any surrounding whitespace
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

# Main function to solve the problem
def main():
    # Input file containing the corrupted memory
    filename = 'input.txt'
    
    # Read the input data from the file
    corrupted_memory = read_input_from_file(filename)
    
    # If the file is successfully read
    if corrupted_memory:
        # Call the function to solve the problem and print the result
        result = solve_corrupted_memory(corrupted_memory)
        print(f"Total sum of multiplications: {result}")
    else:
        print("No valid input to process.")

# Execute the main function
if __name__ == "__main__":
    main()