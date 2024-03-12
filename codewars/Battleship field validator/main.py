def check_diagonals(cell):
    if cell[0][0] == 1 and cell[1][1] == 1:
        return False
    if cell[1][0] == 1 and cell[0][1] == 1:
        return False
    return True

def check_placement(field, height, width):
    for y in range(height - 1):
        for x in range(width - 1):
            cell = [
                [field[y][x], field[y][x + 1]],
                [field[y + 1][x], field[y + 1][x + 1]],
            ]
            if not check_diagonals(cell):
                return False
    return True

def validate_battlefield(field):
    # Check ship placement.
    height = len(field)
    width = len(field[0])
    if not check_placement(field, height, width):
        return False

    # Count ships.
    ship_count = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0
    }
    for y in range(height):
        for x in range(width):
            if field[y][x] == 0:
                continue
            length = 1
            row = field[y][x + 1:]
            column = []
            for i in range(y + 1, 10):
                column.append(field[i][x])

            while len(row) != 0 and row[0] == 1:
                length += 1
                row.pop(0)
            new_row = [0 for i in range(10 - len(row))]
            for i in row:
                new_row.append(i)
            field[y] = new_row

            while len(column) != 0 and column[0] == 1:
                length += 1
                column.pop(0)
            new_column = [0 for i in range(10 - len(column))]
            for i in column:
                new_column.append(i)
            for i in range(10):
                field[i][x] = new_column[i]

            if str(length) not in ship_count:
                return False
            ship_count[str(length)] += 1

    correct_ship_count = {
        '1': 4,
        '2': 3,
        '3': 2,
        '4': 1
    }
    if ship_count != correct_ship_count:
        return False
    return True


# battleField = [
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
# [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

battleField =  [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0]]

# battleField =  [[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(battleField))