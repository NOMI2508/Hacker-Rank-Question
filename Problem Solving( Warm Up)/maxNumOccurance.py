
def birthdayCakeCandles(candles):
    maxCount=0
    maxElement=0
    n=len(candles)
    for i in range(len(candles)):
        count=1
        for j in range(i+1,n):
            if candles[j]==candles[i]:
                count+=1
        if(maxCount<count):
            maxCount=count
            maxElement=candles[i]
    print (maxElement, maxCount)
      
    
candles=[3,2,1,3]

birthdayCakeCandles(candles)
    