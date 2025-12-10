import re
from fractions import Fraction

def parse_input(text):
    machines = []
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Extract targets from {...}
        target_match = re.search(r'\{([0-9,]+)\}', line)
        if not target_match: continue
        targets = [int(x) for x in target_match.group(1).split(',')]
        
        # Extract buttons from (...) between ] and {
        start_idx = line.find(']')
        end_idx = line.find('{')
        if start_idx == -1 or end_idx == -1: continue
        
        button_str = line[start_idx+1:end_idx]
        button_matches = re.findall(r'\(([0-9,]+)\)', button_str)
        
        buttons = []
        for b_str in button_matches:
            indices = [int(x) for x in b_str.split(',')]
            buttons.append(indices)
            
        machines.append({'targets': targets, 'buttons': buttons})
        
    return machines

def solve_machine(machine):
    targets = machine['targets']
    buttons = machine['buttons']
    
    num_vars = len(buttons)  # columns
    num_eqs = len(targets)   # rows
    
    # Build Matrix A: A[row][col] = 1 if button col affects counter row
    A = [[0] * num_vars for _ in range(num_eqs)]
    for col, btn_indices in enumerate(buttons):
        for row in btn_indices:
            if row < num_eqs:
                A[row][col] = 1
                
    b = [Fraction(x) for x in targets]
    M = [[Fraction(x) for x in row] for row in A]
    
    # Gaussian Elimination to RREF
    pivot_row = 0
    pivots = {}  # col -> row
    free_vars = []
    
    for col in range(num_vars):
        if pivot_row >= num_eqs:
            free_vars.append(col)
            continue
            
        # Find pivot in current column
        curr = pivot_row
        while curr < num_eqs and M[curr][col] == 0:
            curr += 1
            
        if curr == num_eqs:
            free_vars.append(col)
            continue
            
        # Swap rows
        M[pivot_row], M[curr] = M[curr], M[pivot_row]
        b[pivot_row], b[curr] = b[curr], b[pivot_row]
        
        # Normalize pivot row
        div = M[pivot_row][col]
        for j in range(col, num_vars):
            M[pivot_row][j] /= div
        b[pivot_row] /= div
        
        # Eliminate other rows
        for i in range(num_eqs):
            if i != pivot_row:
                factor = M[i][col]
                if factor != 0:
                    for j in range(col, num_vars):
                        M[i][j] -= factor * M[pivot_row][j]
                    b[i] -= factor * b[pivot_row]
        
        pivots[col] = pivot_row
        pivot_row += 1
        
    # Check consistency (0 = non-zero means no solution)
    for i in range(pivot_row, num_eqs):
        if b[i] != 0:
            return None
            
    # Calculate bounds for free variables
    var_bounds = [float('inf')] * num_vars
    original_b = machine['targets']
    
    for j in range(num_vars):
        limit = float('inf')
        relevant = False
        for i in range(num_eqs):
            if A[i][j] == 1:
                relevant = True
                limit = min(limit, original_b[i])
        
        if not relevant:
            limit = 0
            
        var_bounds[j] = limit

    # Backtracking search over free variables
    best_total = float('inf')
    
    def backtrack(idx, current_free_vals):
        nonlocal best_total
        
        if idx == len(free_vars):
            # Calculate pivot variables from free variables
            current_x = [0] * num_vars
            current_sum = 0
            
            # Assign free variables
            for f_idx, f_col in enumerate(free_vars):
                val = current_free_vals[f_idx]
                current_x[f_col] = val
                current_sum += val
            
            # Solve for pivots
            possible = True
            for p_col in sorted(pivots.keys(), reverse=True):
                row = pivots[p_col]
                val = b[row]
                for f_col in free_vars:
                    val -= M[row][f_col] * current_x[f_col]
                
                # Check integer and non-negative
                if val.denominator != 1:
                    possible = False
                    break
                val_int = val.numerator
                if val_int < 0:
                    possible = False
                    break
                
                current_x[p_col] = val_int
                current_sum += val_int
            
            if possible and current_sum < best_total:
                best_total = current_sum
            return

        f_col = free_vars[idx]
        limit = var_bounds[f_col]
        
        if limit == float('inf'):
            limit = 0
        
        for val in range(int(limit) + 1):
            backtrack(idx + 1, current_free_vals + [val])

    backtrack(0, [])
    
    return best_total if best_total != float('inf') else None

def solve_part_two(input_text):
    machines = parse_input(input_text)
    total_min_presses = 0
    
    for machine in machines:
        min_presses = solve_machine(machine)
        if min_presses is not None:
            total_min_presses += min_presses
            
    return total_min_presses

if __name__ == "__main__":
    # Test with examples
    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    
    print("Testing examples:")
    test_result = solve_part_two(test_input)
    print(f"Test total: {test_result} (expected 33)")
    
    print("\nSolving actual input:")
    with open("input.txt", "r") as f:
        input_data = f.read()
    result = solve_part_two(input_data)
    print(f"Total minimum button presses: {result}")
