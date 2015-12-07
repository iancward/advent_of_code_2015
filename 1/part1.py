with open('input.txt', 'r') as f:
    input = f.read()

floor = 0
for i in input.rstrip():
    if i == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
