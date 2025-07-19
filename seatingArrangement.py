import math
def arrange(n,r):
    return (math.factorial(n))//math.factorial(n-r)*math.factorial(r)
n=int(input())

r=int(input())
print(arrange(n,r))