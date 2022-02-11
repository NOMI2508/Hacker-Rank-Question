
def diagonalDifference(a):
    # Write your code here
    
    Lsum=0
    Rsum=0
    result=0
    for i in range(len(a)):
        for j in range(len(a)):
            if(i==j):
              Lsum+=a[i][j]
            if(i+j)==(len(a)-1):
              Rsum+=a[i][j]
    return abs(Lsum-Rsum)
    
a=[[1,2,3],[4,5,6],[9,8,9]]


print(diagonalDifference(a))


