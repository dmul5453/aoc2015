input_list = []
sum = 0

with open('2015inputDay2') as f:
    for line in f:
        input_list.append(line)

print(input_list)

def calc_surf_area(l, w, h):
    surface_area = 2*l*w + 2*w*h + 2*h*l
    side1 = l*w
    side2 = l*h
    side3 = h*w
    slack = min(side1, side2, side3)

    total = surface_area + slack
    return total




for i in range(len(input_list)):
    t = 0
    txt = input_list[i]
    args = txt.split("x")
    length = args[0]
    width = args[1]
    height = args[2]
    t = calc_surf_area(int(length), int(width), int(height))
    sum = sum + t

print(sum)
