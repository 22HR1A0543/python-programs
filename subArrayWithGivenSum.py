def subArrayWithGivenSum(arr,n,k): 
    for i in range(n):
        for j in range(1,n):
            if arr[i]+arr[j]==k:
                return arr[i],arr[j]




l=list(map(int,input().split()))
n=len(l)
k=int(input())
print(subArrayWithGivenSum(l,n,k))