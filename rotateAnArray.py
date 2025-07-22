# Rotate an array to right with a value called K
# arr=[1 2 3 4 5 6 7 8]
#step1=[8 1 2 3 4 5 6 7 ]
# step2=[7 8 1 2 3 4 5 6 ]
# step3=[6 7 8 1 2 3 4 5 ]
def rotateArray(arr,n,k):
    print(arr[position:]+arr[0:position])
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
position=n-k  
rotateArray(arr,n,k)
