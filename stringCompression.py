
def stringCompression(s,n):
    for i in s:
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    for key,value in h.items():
        print(f"{key}{value}",end="" )
h={}
s=input()
stringCompression(s,len(s))

#output
#chaithanya
#c1h2a3i1t1n1y1