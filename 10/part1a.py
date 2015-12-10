def look(s):
    i = 0
    to_say = []
    while i < len(s):
        c = 0
        while True:
            try:
                if s[i] == s[i+1]:
                    c += 1
                    i += 1
                else:
                    break
            except IndexError:
                break
        phrase = (c + 1, s[i])
        to_say.append(phrase)
        i += 1
    return to_say

def say(p):
    s = ''
    for t in p:
        s = s + str(t[0]) + t[1]
    return s

steps = 40
start = '1113122113'

seq = [start]
for i in range(0,steps):
    print('step %s' % (i))
    seq.append(say(look(seq[i])))

print("length: %s" % (len(seq[-1])))
