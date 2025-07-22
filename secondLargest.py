def secondlargest(nums,n):
    return sorted(nums)[-2]

nums=list(map(int,input().split()))
n=len(nums)
print(secondlargest(nums,n))