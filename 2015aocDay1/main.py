chars = ''


with open('input2015day1') as f:
    chars = f.read()



current_floor = 0

for i in range(len(chars)):
    if chars[i] == '(':
        current_floor = current_floor + 1
    elif chars[i] == ')':
        current_floor = current_floor - 1

    if current_floor < 0:
        print(i + 1)
        break

print(current_floor)