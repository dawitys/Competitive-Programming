#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    for a_index, value in enumerate(a):
        if value > x:
            a_index -= 1
            break
        x -= value
    max_picks = a_index + 1
    # try filling b removing from a when necessary
    for b_index, value in enumerate(b):
        while value > x and a_index >= 0:
            x += a[a_index]
            a_index -= 1
        if value > x:
            return max_picks
        max_picks = max(max_picks, b_index + a_index + 2)
        x -= value
    return max_picks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
