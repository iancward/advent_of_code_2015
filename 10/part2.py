from itertools import groupby
def step(s):
    next = ''
    for k, g in groupby(s):
        next = next + str(len(list(g))) + k
    return next

def iterate(s, i):
    results =[s]
    for st in range(0,i):
        results.append(step(results[-1]))

    return results

input = '1113122113'
steps = 50

my_list = iterate(input, steps)
print(len(my_list[-1]))
