def max_ele(arr):
    minii=arr[0]
    for i in range(1,n):
        if arr[i]<minii:
            minii=arr[i]

    return minii
arr=list(map(int,input().split()))
n=len(arr)
print(max_ele(arr))