def triangle(row):
    newrow = ''
    while len(row) > 2:
        for i in range(len(row) - 2):
            triplet = row[i:i+3]
            # print(triplet)

            # case 1. -> all same -> same goes
            if (triplet[0] == triplet[1] and
                triplet[1] == triplet[2]):
                newrow += triplet[1]
                continue

            # case 2. -> all different -> middle goes
            if (triplet[0] != triplet[1] and
                triplet[1] != triplet[2] and
                triplet[0] != triplet[2]):
                newrow += triplet[1]
                continue

            # case 3. -> sides same -> third goes
            if triplet[0] == triplet[2]:
                if 'G' not in triplet:
                    newrow += 'G'
                    continue
                if 'R' not in triplet:
                    newrow += 'R'
                    continue
                if 'B' not in triplet:
                    newrow += 'B'
                    continue

            # case 4. -> same beside eachother -> extra goes
            if triplet[0] == triplet[1]:
                newrow += triplet[2]
                continue
            if triplet[1] == triplet[2]:
                newrow += triplet[0]
                continue

        row = newrow
        newrow = ''

    if len(row) == 1:
        return row

    # the length is 2
    if row[0] == row[1]:
        return row[0]
    if 'G' not in row:
        return 'G'
    if 'R' not in row:
        return 'R'
    return 'B'

print(triangle('RBRGBRBGGRRRBGBBBGG'))
# print(triangle('RBR'))