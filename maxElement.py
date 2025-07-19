def max_ele(arr):
    maxi=arr[0]
    for i in range(1,n):
        if arr[i]>maxi:
            maxi=arr[i]

    return maxi
arr=list(map(int,input().split()))
n=len(arr)
print(max_ele(arr))