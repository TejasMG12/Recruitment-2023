r=int(input("Enter red value:"))
g=int(input("Enter green value:"))
b=int(input("Enter blue value:"))
if r>=155 and g <=100 and b<= 100:
    print("The color is Red")
elif r<=100 and g >= 155 and b<= 100:
    print("The color is Green")
elif r<=100 and g <=100 and b>= 155:
    print("The color is Blue")
elif r>=155 and g >= 155 and b>= 155:
    print("The color is White")
elif r<=155 and g <= 155 and b<= 155:
    print("The color is grey")
elif r>=155 and g >= 155 and b<= 155:
    print("The color is Yellow")
elif r<=155 and g >= 155 and b>= 155:
    print("The color is Aqua")
elif r>=155 and g <= 155 and b>= 155:
    print("The color is Purple")