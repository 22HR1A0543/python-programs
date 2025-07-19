#sum of elements that the greater than k
def arrayRangeSum(arr,n,k):
    sum=0
    for i in arr:
        if i>k:
            sum+=i
    print(sum)
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
arrayRangeSum(arr,n,k)