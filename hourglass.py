#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = float('-inf')
    
    # Iterate through all possible hourglass top-left positions
    # Hourglass spans 3 rows and 3 columns, so we can start from (0,0) to (3,3)
    for i in range(4):
        for j in range(4):
            # Calculate hourglass sum
            # Top row: arr[i][j], arr[i][j+1], arr[i][j+2]
            # Middle: arr[i+1][j+1]
            # Bottom row: arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
            hourglass = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                         arr[i+1][j+1] +
                         arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
            max_sum = max(max_sum, hourglass)
    
    return max_sum

if __name__ == '__main__':
    OUTPUT_PATH = "C:/Users/Manpreet/OneDrive - City St George\'s, University of London/Documents/Term1/Interview Resources/HackerRank/hourglass.txt"
    fptr = open(OUTPUT_PATH, 'w')

    #arr = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","
    # ","0 0 0 2 0 0","0 0 1 2 4 0"]
    arr=[]
    #arr.append(list(map(int, input("1 1 1 0 0 0").rstrip().split())))
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
