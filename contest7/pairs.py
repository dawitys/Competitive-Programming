#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    result = 0
    arr = sorted(arr)
    j = 1
    for i in range(len(arr)-1):
        while j<len(arr):
            if arr[j] - arr[i] == k:
                result += 1
                j += 1
            elif arr[j] - arr[i] > k:
                break
            elif arr[j] - arr[i] < k:
                j += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
