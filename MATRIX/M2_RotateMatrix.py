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




"""def rotate90Clockwise(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

    for i in range(n//2):
        for j in range(n):
            arr[j][i],arr[j][n-i-1]=arr[j][n-i-1],arr[j][i]
    return arr 


def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])


A = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

printMatrix(A)
A=rotate90Clockwise(A)
print()
printMatrix(A)"""
