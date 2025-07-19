#def removeDs(s):
s="chaithanya"
#print(''.join(set(s)))
h=[]
for i in s:
    if i  not in h:
        h.append(i)
for i in h:
    print(i,end=" ")
