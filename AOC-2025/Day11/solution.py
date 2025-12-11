def solve():
    # Read input from file
    with open("input.txt", "r") as f:
        puzzle_input = f.read()
    
    # Parse the Input into a Graph (Adjacency List)
    graph = {}
    lines = [line.strip() for line in puzzle_input.split('\n') if line.strip()]
    
    for line in lines:
        parts = line.split(':')
        source = parts[0].strip()
        if len(parts) > 1:
            destinations = parts[1].strip().split()
            graph[source] = destinations
        else:
            graph[source] = []

    # Part 1: Count all paths from "you" to "out" using memoization
    memo1 = {}

    def count_paths_from(node):
        if node == 'out':
            return 1
        if node not in graph:
            return 0
        if node in memo1:
            return memo1[node]
        
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths_from(neighbor)
        
        memo1[node] = total_paths
        return total_paths

    result1 = count_paths_from('you')
    print(f"Part 1 - Total paths from 'you' to 'out': {result1}")

    # Part 2: Count paths from "svr" to "out" visiting both "dac" and "fft"
    # Memo key: (node_name, visited_dac, visited_fft)
    memo2 = {}

    def count_paths_with_required(node, visited_dac, visited_fft):
        # Update flags if current node is one of the required ones
        if node == 'dac':
            visited_dac = True
        if node == 'fft':
            visited_fft = True

        # Base Case: Reached the target
        if node == 'out':
            return 1 if visited_dac and visited_fft else 0
        
        # Base Case: Dead end
        if node not in graph:
            return 0
        
        # Check Cache
        state_key = (node, visited_dac, visited_fft)
        if state_key in memo2:
            return memo2[state_key]
        
        # Recursive Step
        total_paths = 0
        for neighbor in graph[node]:
            total_paths += count_paths_with_required(neighbor, visited_dac, visited_fft)
        
        memo2[state_key] = total_paths
        return total_paths

    result2 = count_paths_with_required('svr', False, False)
    print(f"Part 2 - Paths from 'svr' to 'out' visiting both 'dac' and 'fft': {result2}")

    return result1, result2

if __name__ == "__main__":
    solve()
