

def plusMinus(array):
    positiveNum=0
    negativeNum=0
    zeroNum=0
    pString=[]
    li=[]
    for i in range(len(array)):
        if array[i]>0:
            positiveNum+=1
        elif array[i]<0:
            negativeNum+=1
        else:
            zeroNum+=1
    
    positiveNum/=len(array)
    li.append(positiveNum)
    negativeNum/=len(array)
    li.append(negativeNum)
    zeroNum/=len(array)
    li.append(zeroNum)
    for i in range(len(li)):
     print('{0:.6f}'.format(li[i]))
   
    
    
array=[1,1,0,-1,-1]
    
plusMinus(array)