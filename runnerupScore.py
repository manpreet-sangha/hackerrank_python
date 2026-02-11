from array import array
#import numpy as np
# I want to use numpy to find the runner up score in a list of scores. 
# numpy is memory efficient and fast for large lists of scores, so it is a good choice for this problem.

def runnerupScore(n, arr):
    # use the numpy function np.unique to find the unique scores and then sort them to find the second highest score.
    #unique_scores = np.unique(arr)
    #unique_list = list(set(arr))
    #unique_scores = array(i, unique_list)
    
    #sorted_arr = arr.sort()
    
    # sort the unique scores in ascending order and return the second last element, which is the runner up score. If there are less than 2 unique scores, return None.
    #sorted_arr = np.sort(unique_scores)
    
    # Keep only unique elements from the array
    unique_arr = list(set(arr)) 
    sorted_unique_arr = sorted(unique_arr)
        
    if len(sorted_unique_arr) < 2:
        return None
    
    # list[-2] gives the second last element of the list, which is the runner up score.
    
    return sorted_unique_arr[-2]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if ((n<2) or (n>10)):
        raise ValueError("Invalid input: n must be between 2 and 10")

    for i in range(len(arr)):
        if ((arr[i]<-100) or (arr[i]>100)):
            raise ValueError("Invalid input: each element in arr i.e. scores must be between -100 and 100")

    if n != len(arr):
        raise ValueError("Invalid input: n must be equal to the number of scores in arr")
        
    #arr = np.array(list(arr))
    print(runnerupScore(n, arr))
