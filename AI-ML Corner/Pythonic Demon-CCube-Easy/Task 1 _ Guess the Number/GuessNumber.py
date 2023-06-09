import random 
players=[]
points=[]
while(True):
    x=input("Enter your name:").upper()
    if x not in players:
        players.append(x)
        points.append(100)
    i=players.index(x)
    a=int(input("Enter the lower limit:"))
    b=int(input("Enter the upper limit:"))
    x=random.randint(a,b)
    z=(b-a)/3
    y=int(input("Enter your guess:"))
    if x!=y:
        points[i]-=5
        if  x>y+z :
            print("guess too low") 
        elif x< y-z :
            print("Guess too high")
        print("You have %s points left"%(points[i]))
    else:
        print("congrats %s you won with %s points"%(players[i], points[i]))
        break
    if points[i]==0:
        print("you ran out of points")
        break