def reverse_array(arr,n):
    return arr[::-1]
arr=list(map(int,input().split()))
n=len(arr)
print(reverse_array(arr,n))