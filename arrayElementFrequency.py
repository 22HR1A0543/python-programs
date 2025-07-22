# l=[1 1 1 6 7 8]
# ele=1
# frequency=3
def arrayEleFrequency(arr,n,ele):
    return arr.count(ele)
arr=list(map(int,input().split()))
n=len(arr)
ele=int(input())
print(arrayEleFrequency(arr,n,ele))