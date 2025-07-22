def arrayAvg(arr,n):
    return sum(arr)//n
arr=list(map(int,input().split()))
n=len(arr)
print(arrayAvg(arr,n))
