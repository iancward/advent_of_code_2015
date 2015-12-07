import hashlib

target = '000000'
input = 'iwrupvqb'

counter = 0

while True:
    i = input + str(counter)
    hash = hashlib.md5(i.encode('ascii')).hexdigest()
    if hash.startswith(target):
        print('counter: %s' % (counter))
        break
    counter += 1
