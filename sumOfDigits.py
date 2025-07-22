def sumOfDigits(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    print(sum)

n=int(input())
sumOfDigits(n)