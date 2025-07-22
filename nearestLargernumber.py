def nearestLargerNumber(arr,n,k):
    
    for i in arr:
        if i>k:
            largerElements.append(i)
    return sorted(largerElements)[0]

largerElements=[]
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(nearestLargerNumber(arr,n,k))
