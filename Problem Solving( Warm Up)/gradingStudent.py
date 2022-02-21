import math




def grading(arr):
    divisonNum=0
    differenceNum=0
    nArray=[]
    for i in range(len(arr)):
        divisonNum=math.ceil(arr[i]/5)
        divisonNum+=1
        divisonNum*=5
        differenceNum=divisonNum-arr[i]
        if(differenceNum<3):
            nArray[i].append(divisonNum)
        else:
            nArray[i].append(arr[i])
        print(nArray)
       
        
        











arr=[73,67,38,33]
grading(arr)