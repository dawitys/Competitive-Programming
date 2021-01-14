#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.

def superDigit(n, k):
    digits = map(int, list(n))
    return superDigits(str(sum(digits) * k))

def superDigits(p):
    if len(p) == 1:
        return int(p)
    else:
        return superDigits(str(sum(map(int, list(p)))))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
