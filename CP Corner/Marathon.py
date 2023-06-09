
d,a=map(int,input().split())
x=d*a

if x>=45:
    print(3)
elif 45>x>=35:
    print(2)
elif 35>x>=15:
    print(1)
else :
    print(-1)
