def mergeSortingArray(l1,l2,n):
    #print(sorted(l2+l1))
    for i in l2:
        l1.append(i)
    print("before sorting:",l1)
    l1.sort()
    print("after sorting",l1)
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n=len(l1)
mergeSortingArray(l1,l2,n)