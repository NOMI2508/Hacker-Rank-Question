
def diagonalDifference(arr):
    # Write your code here
    
    Lsum=0
    Rsum=0
    result=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i==j):
              Lsum+=array[i][j]
            if(i+j)==(len(array)-1):
              Rsum+=array[i][j]
    return abs(Lsum-Rsum)
    
array=[[1,2,3],[4,5,6],[9,8,9]]


print(diagonalDifference(array))


