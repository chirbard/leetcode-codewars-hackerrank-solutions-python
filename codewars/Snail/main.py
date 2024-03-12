# Solution with recursion (by me)
def upper_list(result, lst):
    for element in lst:
        result.append(element)

def lower_list(result, lst):
    for element in reversed(lst):
        result.append(element)

def edge_cases(result, snail_map):
    if len(snail_map) == 0:
        return result
    if len(snail_map) == 1:
        upper_list(result, snail_map.pop(0))
        return result
    if len(snail_map) == 2:
        upper_list(result, snail_map.pop(0))
        lower_list(result, snail_map.pop(0))
        return result

def recursion_loop(result, snail_map):
    if len(snail_map) < 3:
        return edge_cases(result, snail_map)

    upper_list(result, snail_map.pop(0))
    for i in range(len(snail_map) - 1):
        result.append(snail_map[i].pop(-1))

    lower_list(result, snail_map.pop(len(snail_map) - 1))
    for i in range(len(snail_map) - 1, 0, -1):
        result.append(snail_map[i].pop(0))

    return recursion_loop(result, snail_map)

def snail(snail_map):
    result = []
    return recursion_loop(result, snail_map)

# Solution using Numpy (from CodeWars)
# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

array = [[1,2,3,4],
         [8,9,4,5],
         [1,2,3,4],
         [7,6,5,6]]
print(snail(array))