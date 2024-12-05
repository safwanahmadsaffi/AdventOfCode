def read_input(file_path):
    """Reads the input grid from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_xmas_in_grid(grid):
    """Finds all occurrences of the word 'XMAS' in the grid."""
    word = "XMAS"
    word_length = len(word)
    num_rows = len(grid)
    num_cols = len(grid[0])
    count = 0

    # Directions for checking:
    # (row_change, col_change) for the 8 possible directions
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # top-left diagonal
        (-1, 1),  # top-right diagonal
        (1, -1),  # bottom-left diagonal
        (1, 1)    # bottom-right diagonal
    ]

    # Function to check if "XMAS" can be found from a given start position
    def is_valid_direction(r, c, dr, dc):
        """Check if 'XMAS' can be formed starting from (r, c) in direction (dr, dc)."""
        for i in range(word_length):
            new_r, new_c = r + i * dr, c + i * dc
            if not (0 <= new_r < num_rows and 0 <= new_c < num_cols):  # Out of bounds
                return False
            if grid[new_r][new_c] != word[i]:  # Character mismatch
                return False
        return True

    # Iterate over each cell in the grid
    for r in range(num_rows):
        for c in range(num_cols):
            # Check in all 8 possible directions
            for dr, dc in directions:
                if is_valid_direction(r, c, dr, dc):
                    count += 1

    return count

# Main function to execute the puzzle solution
def main():
    # File path to input.txt
    input_file = 'input.txt'
    
    # Read the grid from the file
    grid = read_input(input_file)
    # Find all occurrences of "XMAS" in the grid
    result = find_xmas_in_grid(grid)
    # Output the result
    print(f"The word 'XMAS' appears {result} times.")

# Run the main function
if __name__ == "__main__":
    main()