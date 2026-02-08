#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    total_bribes = 0
    
    # Check each person in the queue
    for i in range(len(q)):
        # q[i] is the person's original position (1-indexed)
        # i is their current position (0-indexed)
        # If person moved more than 2 positions forward, it's chaotic
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # Count how many people with higher numbers are ahead of this person
        # These are the people who bribed past this person
        # We only need to check from max(0, q[i]-2) to i
        # because person q[i] could have started at position q[i]-1 (0-indexed)
        # and moved back at most to position q[i]-2 due to bribes
        # if q[i] == i+1:
        #      continue
        # elif q[i] == i+2:
        #     total_bribes += 1
        # elif q[i] == i+3:
        #     total_bribes += 2
        # elif q[i] > i+3:
        #     print("Too chaotic")
        #     return
        
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total_bribes += 1

    print(total_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)