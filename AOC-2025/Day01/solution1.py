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
            
        # Match L or R followed by digits
        match = re.match(r'^([LR])(\d+)$', line)
        if not match:
            continue
            
        direction = match.group(1)
        amount = int(match.group(2))
        
        if direction == 'L':
            dial = (dial - amount) % 100
        elif direction == 'R':
            dial = (dial + amount) % 100
            
        if dial == 0:
            count += 1
            
    print(f"Password: {count}")

if __name__ == '__main__':
    solve()
