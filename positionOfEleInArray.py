def position(arr,n,target):
    #return arr.index(target)
    count=0
    for i in range(n):
        if arr[i]==target:
            return i
        


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(position(arr,n,target))