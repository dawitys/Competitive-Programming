#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    available_colors = dict()
    pairs = 0
    for i in ar:
        if (i in available_colors.keys()) and available_colors[i] == 1:
            available_colors[i] = 0
            pairs += 1
        elif (i in available_colors.keys()) and available_colors[i] == 0:
            available_colors[i] += 1
        else:
            available_colors[i] = 1
        print(available_colors)
    return pairs
            
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
