input_list = []
sum = 0

with open('2015inputDay2') as f:
    for line in f:
        input_list.append(line)

print(input_list)

def calc_ribbon(l, w, h):
    perimeter1 = 2 * (l + w)
    perimeter2 = 2 * (l + h)
    perimeter3 = 2 * (h + w)
    ribbon_length = min(perimeter1, perimeter2, perimeter3)
    bow_length = l * w * h
    return ribbon_length + bow_length


for i in range(len(input_list)):
    t = 0
    txt = input_list[i]
    args = txt.split("x")
    length = args[0]
    width = args[1]
    height = args[2]

    t = calc_ribbon(int(length), int(width), int(height))
    sum = sum + t

print(sum)