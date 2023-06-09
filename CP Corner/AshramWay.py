a = list(map(int,input().strip().split()))
if a[2]!=0 and a[0]%a[2]==0 and a[1]%a[2]==0:
    print("YES")
else:
    print("NO")
