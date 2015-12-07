import operator
import functools

with open('input.txt', 'r') as f:
    input = f.read()

stuff = input.rstrip().split('\n')
list = []
for box in stuff:
    list.append([int(i) for i in box.split('x')])

total_area = 0
for box in list:
    box.sort()
    total_area += 2 * (box[0] + box[1])
    total_area += functools.reduce(operator.mul, box)

print(total_area)
