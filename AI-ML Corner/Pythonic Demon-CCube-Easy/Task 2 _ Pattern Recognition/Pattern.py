

def pat(l,n):
    if len(l)%n!=0:
        return 0
    L=len(l)
    for i in range(L-n):
        j=i
        while(j<L-n):
            if l[j]!=l[j+n]:
                return 0
            j=j+n
    return 1
                
print("Enter the list:")
l=input().strip().split(',')
l[0]=l[0][1:]
l[-1]=l[-1][:-1]
for i in range(len(l)):
    l[i]=int(l[i])

for i in range(len(l)//2 +1):
    x=pat(l,i+1)
    if x==1:
        print("Pattern Found:",l[:i+1])
        print("It repeats %s times"%(len(l)//(i+1)))
        break
if x==0:
    print("Pattern not found")