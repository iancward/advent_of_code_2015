def move(location, direction):
    if action == '^':
        location[1] += 1
    elif action == 'v':
        location[1] -= 1
    elif action == '>':
        location[0] += 1
    elif action == '<':
        location[0] -= 1

with open('input.txt', 'r') as f:
    input = f.read()

santa_location = [0,0]
robo_location = [0,0]
robo = False

visited_locations = []
visited_locations.append(santa_location[:])

for action in input.rstrip():
    if robo == False:
        move(santa_location, action)
        if santa_location not in visited_locations:
            visited_locations.append(santa_location[:])
    else:
        move(robo_location, action)
        if robo_location not in visited_locations:
            visited_locations.append(robo_location[:])
    # switch people
    robo = not robo

print(len(visited_locations))
