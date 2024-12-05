def parse_input(file_path):
    with open(file_path, "r") as file:
        sections = file.read().strip().split("\n\n")
        rules = [tuple(map(int, line.split("|"))) for line in sections[0].split("\n")]
        updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]
    return rules, updates
def validate_update(update, precedence_rules):
    for x, y in precedence_rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True
def find_middle_sum(file_path):
    rules, updates = parse_input(file_path)
    # Validate updates
    valid_updates = []
    for update in updates:
        if validate_update(update, rules):
            valid_updates.append(update)
    # Calculate the middle page sum
    middle_sum = sum(update[len(update) // 2] for update in valid_updates)
    return middle_sum
# File path to the input data
file_path = "input.txt"
# Find and print the middle sum
result = find_middle_sum(file_path)
print(f"Sum of middle page numbers from correctly ordered updates: {result}")