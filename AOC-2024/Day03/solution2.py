
def evaluate_instructions(instructions):
    # Initialize the state
    enabled = True  # Mul instructions are enabled by default
    total_sum = 0

    # Regular expression to match mul(x, y), do(), and don't() instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r'don\'t\(\)')
    
    i = 0
    while i < len(instructions):
        # Check for 'mul(x, y)' pattern
        mul_match = mul_pattern.match(instructions, i)
        if mul_match:
            x = int(mul_match.group(1))
            y = int(mul_match.group(2))
            if enabled:
                total_sum += x * y
            i = mul_match.end()
            continue
        
        # Check for 'do()' pattern
        if do_pattern.match(instructions, i):
            enabled = True  # Enable future mul instructions
            i = do_pattern.match(instructions, i).end()
            continue
        
        # Check for 'don't()' pattern
        if dont_pattern.match(instructions, i):
            enabled = False  # Disable future mul instructions
            i = dont_pattern.match(instructions, i).end()
            continue
        
        # If we reach here, just move to the next character
        i += 1

    return total_sum

def main():
    # Read the instructions from input.txt
    with open('input.txt', 'r') as file:
        instructions = file.read().strip()
    
    # Evaluate the instructions
    result = evaluate_instructions(instructions)
    
    # Print the result
    print(f"The total sum of enabled multiplications is: {result}")

if __name__ == "__main__":
    main()