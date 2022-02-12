
def miniMaxSum(arr,n):
    max_sum = 0
    min_sum=0
    left=[0]*n
    right=[0]*n
    sum=[0]*n
    
    left[0]=0
    right[n-1]=0
    
    for i in range(1,n):
        left[i]=arr[i-1]+left[i-1]
    for j in range(n-1,0, -1):
        right[j-1] = arr[j ] + right[j ]
        
    for i in range(n):
        sum[i]=left[i] + right[i]
    
    
    max_sum=max(sum)
    min_sum=min(sum)
    print (min_sum,max_sum)
    
    
    
    
arr = [1,2,3,4,5]
n = len(arr)

miniMaxSum(arr,n)
    