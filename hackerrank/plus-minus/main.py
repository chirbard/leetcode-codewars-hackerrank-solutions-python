#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    value_counts = {
        '+': 0,
        '-': 0,
        '0': 0,
    }
    for num in arr:
        if num < 0:
            value_counts['-'] += 1
            continue
        if num == 0:
            value_counts['0'] += 1
            continue
        value_counts['+'] += 1
    
    total = len(arr)
    print(round(value_counts['+']/total, 6))
    print(round(value_counts['-']/total, 6))
    print(round(value_counts['0']/total, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
