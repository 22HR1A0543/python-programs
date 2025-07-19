def countEvenOdd(arr,n):
    evenCount=0
    oddCount=0
    for i in arr:
        if(i%2)==0:
            evenCount+=1
        else:
            oddCount+=1
    print(evenCount,oddCount)
arr=list(map(int,input().split()))
n=len(arr)
countEvenOdd(arr,n)

