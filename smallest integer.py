a=int(input("enter the first integer"))
b=int(input("enter the second integer"))
c=int(input("enter the third integer"))
if (a<=b and b<=c):
    print("a is the smallest integer")
elif(b<=a and b<c):
    print("b is the smallest integer")
else:
    print("c is the smallest integer")
