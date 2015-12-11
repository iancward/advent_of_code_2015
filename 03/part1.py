with open('input.txt', 'r') as f:
    input = f.read()

my_location = [0,0]
visited_locations = []

visited_locations.append(my_location[:])

for action in input.rstrip():
    if action == '^':
        my_location[1] += 1
    elif action == 'v':
        my_location[1] -= 1
    elif action == '>':
        my_location[0] += 1
    elif action == '<':
        my_location[0] -= 1
    else:
        print("Invalid input!")
        break

    if my_location not in visited_locations:
        visited_locations.append(my_location[:])

print(len(visited_locations))
