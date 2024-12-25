from collections import defaultdict

def parse_input(input_text):
    wires = {}
    operations = []
    for line in input_text.strip().split('\n'):
        if ':' in line:
            wire, value = line.split(':')
            wires[wire.strip()] = int(value.strip())
        elif '->' in line:
            operations.append(line.strip())
    return wires, operations

def evaluate_gate(op, a, b):
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b
    return 0

def process_operations(wires, operations):
    resolved = set(wires.keys())
    pending = operations[:]
    
    while pending:
        next_pending = []
        for operation in pending:
            parts = operation.split()
            if len(parts) == 5:
                a, op, b, _, dest = parts
                if a in wires and b in wires:
                    wires[dest] = evaluate_gate(op, wires[a], wires[b])
                    resolved.add(dest)
                else:
                    next_pending.append(operation)
            elif len(parts) == 4:
                a, op, _, dest = parts
                if a in wires:
                    wires[dest] = evaluate_gate(op, wires[a], 0)
                    resolved.add(dest)
                else:
                    next_pending.append(operation)
        pending = next_pending
    
    return wires

def extract_z_values(wires):
    z_values = {k: v for k, v in wires.items() if k.startswith('z')}
    sorted_bits = [z_values[f'z{i:02}'] for i in range(len(z_values))]
    binary_number = ''.join(map(str, sorted_bits[::-1]))
    return int(binary_number, 2)

def main(input_text):
    wires, operations = parse_input(input_text)
    wires = process_operations(wires, operations)
    result = extract_z_values(wires)
    print('Decimal Output:', result)

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_text = file.read()
    main(input_text)