#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    
    while i < len(c) - 1:
        # Try to jump 2 clouds if possible (greedy approach)
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps

if __name__ == '__main__':
    #OUTPUT_PATH = "C:/Users/Manpreet/OneDrive - City St George\'s, University of London/Documents/Term1/Interview Resources/hackerrank_python/jumpingOnClouds.txt"
    OUTPUT_PATH = os.environ.get('OUTPUT_PATH', 'jumpingOnClouds.txt')
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
