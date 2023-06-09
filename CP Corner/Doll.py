n=int(input())
d=[]
c=[]
for i in range(n):
    x=int(input())
    if x not in(d):
        d.append(x)
        c.append(1)
    else:
        j =d.index(x)
        c[j]+=1
for i in range(len(d)):
    if c[i]%2==1:
        print(d[i])
        break
