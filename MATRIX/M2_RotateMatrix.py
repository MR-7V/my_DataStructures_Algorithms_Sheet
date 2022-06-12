#https://leetcode.com/problems/rotate-image/

def rotate90Clockwise(arr):
    l,r = 0,len(arr)-1

    while l < r:
        for i in range(r-l):
            top,bottom = l,r 
            topLeft = arr[top][l+i]
            arr[top][l+i] = arr[bottom-i][l]
            arr[bottom-i][l] = arr[bottom][r-i]
            arr[bottom][r-i] = arr[top+i][r]
            arr[top+i][r] = topLeft 
        l+=1
        r-=1
    return arr

def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])

A = [[1,2,3],[4,5,6],[7,8,9]]

A=rotate90Clockwise(A)
printMatrix(A)

"""
Output: 
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]

Reference: https://www.youtube.com/watch?v=fMSJSS7eO1w"""
