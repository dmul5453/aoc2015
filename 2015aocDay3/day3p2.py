with open('2015inputDay3') as f:
    input = f.read()
print(input)

test_input = "^v^v^v^v^v"

x_pos = 0
y_pos = 0

found_pairs = set()

found_pairs.add((0,0))

for x in input[::2]:
    instruction = x
    if instruction == "^":
        y_pos = y_pos + 1
    elif instruction == "v":
        y_pos = y_pos - 1
    elif instruction == ">":
        x_pos = x_pos + 1
    elif instruction == "<":
        x_pos = x_pos - 1

    found_pairs.add((x_pos, y_pos))

x_pos = 0
y_pos = 0

for x in input[1::2]:
    instruction = x
    if instruction == "^":
        y_pos = y_pos + 1
    elif instruction == "v":
        y_pos = y_pos - 1
    elif instruction == ">":
        x_pos = x_pos + 1
    elif instruction == "<":
        x_pos = x_pos - 1

    found_pairs.add((x_pos, y_pos))

print(len(found_pairs))