def move_zeros(lst):
    length = len(lst)

    i = 0
    while i < length:
        if lst[i] == 0:
            length -= 1
            lst.pop(i)
            lst.append(0)
            continue
        i += 1

    return lst

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))