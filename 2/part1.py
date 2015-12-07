with open('input.txt', 'r') as f:
    input = f.read()

stuff = input.rstrip().split('\n')
list = []
for box in stuff:
    list.append([int(i) for i in box.split('x')])

total_area = 0
for box in list:
    area = []
    area.append(box[0] * box[1])
    area.append(box[0] * box[2])
    area.append(box[1] * box[2])
    total_area += 2 * sum(area) + min(area)

print(total_area)
