def spiralPrint(arr):
    result=[]
    top = 0
    bottom = len(arr)
    left = 0
    right = len(arr[0])
    
    while (top != bottom and right!=left):
        for i in range(left,right):
            result.append(arr[top][i])
        top+=1

        for i in range(top,bottom):
            result.append(arr[i][right-1])
        right-=1

        if (top != bottom and right!=left):
            for i in range(right-1,left-1,-1):
                result.append(arr[bottom-1][i])
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                result.append(arr[i][left])
            left+=1 
    return result


arr = [ [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]
print(spiralPrint(arr))


#Output : [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
#Reference : https://www.youtube.com/watch?v=BJnMZNwUk1M