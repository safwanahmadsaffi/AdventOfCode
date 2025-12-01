import re

def solve():
    dial = 50
    count = 0
    
    with open('input1.txt', 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = re.match(r'^([LR])(\d+)$', line)
        if not match:
            continue
            
        direction = match.group(1)
        amount = int(match.group(2))
        
        if direction == 'L':
            dist_to_0 = dial if dial != 0 else 100
            if amount >= dist_to_0:
                count += 1 + (amount - dist_to_0) // 100
            dial = (dial - amount) % 100
            
        elif direction == 'R':
            dist_to_0 = (100 - dial) if dial != 0 else 100
            if amount >= dist_to_0:
                count += 1 + (amount - dist_to_0) // 100
            dial = (dial + amount) % 100
            
    print(f"Password: {count}")

if __name__ == '__main__':
    solve()
