def even_odd_count(arr):
    evencount=0
    oddcount=0
    for i in arr:
        if i%2==0:
            evencount+=1
        else:
            oddcount+=1
    return evencount,oddcount
arr=list(map(int,input().split()))
print(even_odd_count(arr))