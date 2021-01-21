#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repeatAmount = n//len(s)
    numberEdgeSubString = s[:(n%len(s))].count('a')
    aIns = list(s).count('a')
    return (repeatAmount * aIns) + numberEdgeSubString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
