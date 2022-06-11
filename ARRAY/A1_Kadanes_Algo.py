from sys import maxsize

def maxSubArraySum(arr):
    max_so_far = -maxsize-1
    curr_max = start = end = s = 0
    
    for i in range(len(arr)):
        curr_max += arr[i]

        if max_so_far < curr_max:
            max_so_far = curr_max
            start = s 
            end = i 

        if curr_max < 0:    #this cond will also handle if all numbers are - ve by returning least -ve number.
            curr_max = 0
            s = i+1
    print(max_so_far)
    print(arr[start:end+1])

arr = [-2, -3, -4, 1, 2, -1, 5, -3]
maxSubArraySum(arr)