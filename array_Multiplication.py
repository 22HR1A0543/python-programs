def array_multiplication(list1,list2,n):
    l=[]
    for i in range(n):
        l.append(list1[i]*list2[i])
    return l
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
n=len(list1)
print(array_multiplication(list1,list2,n))