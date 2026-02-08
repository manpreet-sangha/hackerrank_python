#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    
    number_of_pairs = 0
    distinct_colors_arr = list(set(ar))
    print(distinct_colors_arr)
    #sorted_arr = sorted(ar)
    for i in range(len(distinct_colors_arr)):
        number_of_socks = ar.count(distinct_colors_arr[i])
        print("number_of_socks of color "+str(distinct_colors_arr[i])+ " : "+str(number_of_socks))
        number_of_pairs += math.floor(number_of_socks/2)
        print("Total number_of_pairs: "+str(number_of_pairs))
    return number_of_pairs     
        

if __name__ == '__main__':
    OUTPUT_PATH = "C:/Users/Manpreet/OneDrive - City St George\'s, University of London/Documents/Term1/Interview Resources/hackerrank_python/sockMerchant.txt"
    fptr = open(OUTPUT_PATH, 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
