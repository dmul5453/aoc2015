with open('2015inputDay3') as f:
    input = f.read()
print(input)

test_input = "^>v<"

x_pos = 0
y_pos = 0

found_pairs = set()

found_pairs.add((0,0))

#   in_set = (0,0) in found_pairs
#   print(in_set)

for i in range(len(input)):
    instruction = input[i]
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
