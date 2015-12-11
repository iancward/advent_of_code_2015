with open('input.txt', 'r') as f:
    input = f.read()

floor = 0
for i in range(0, len(input.rstrip())):
    if input[i] == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i+1)
        break

