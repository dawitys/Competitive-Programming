#!/bin/python3

import math
import os
import random
import re
import sys

def bound(x, y ,  mat):
    return 0 <= x < len(mat) and 0<= y < len(mat[0])
    
def surfaceArea(A):
    

    x,y = len(A),len(A[0])
    area = 0
    moves = [[0,1],[1,0],[-1,0],[0,-1]]
    for i in range(x):
        for j in range(y):
            for k,l in moves:
                cArea = A[i][j]
                e,f = k + i,l+ j
                area += max(0,cArea - A[e][f]) if bound(e,f,A) else cArea 
                
    TxB  = x * y * 2
    return  TxB + area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
