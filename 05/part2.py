def repeating_pair(s):
    repeating_chars = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            # we don't want to loop around backwards
            if i == 1:
                repeating_chars += 1
            # don't increment if repeats overlap
            elif s[i] != s[i-2]:
                repeating_chars += 1
    if repeating_chars >= 2:
        return True
    else:
        return False


def vowel_test(s):
    vowel_count = 0
    for c in 'aeiou':
        vowel_count += s.count(c)
        # we only need 3 vowels
        if vowel_count >= 3:
            break

    # if we found fewer than three vowels,
    # this isn't a good word
    if vowel_count < 3:
        return False
    else:
        return True

def repeating_chars(s):
    repeating_chars = False
    for i, c in enumerate(s):
        # don't check past end of string
        if i == len(s) - 1:
            break

        if c == s[i + 1]:
            repeating_chars = True
            break
    return repeating_chars

def no_bad_strings(s):
    has_bad_string = False
    # check if string contains bad substrs
    for bad in ['ab', 'cd', 'pq', 'xy']:
        if bad in s:
            has_bad_string = True
            break
    return not has_bad_string

with open('input.txt', 'r') as f:
    input = f.read()

good_strings = 0
for s in input.split('\n'):
    if all([vowel_test(s), repeating_chars(s), no_bad_strings(s)]):
        good_strings += 1

print(good_strings)
