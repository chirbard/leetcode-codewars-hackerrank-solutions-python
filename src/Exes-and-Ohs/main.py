def xo(s):
    s = s.lower()
    hashmap = {
        'x': 0,
        'o': 0
    }
    for char in s:
        if char in hashmap:
            hashmap[char] += 1

    if hashmap['x'] == hashmap['o']: return True
    return False

print(xo('xooox'))