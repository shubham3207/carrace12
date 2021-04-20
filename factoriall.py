###wap to find factorial of a number using functions

def fact():
    num=int(input("enter the number of factorial"))
    prod=1
    for i in range(2,num+1):
        prod=prod*i
    for i in range(2,a+1):
        prod=prod*i
    return prod
a=int(input("enter the number for factorial"))
factorial=fact(a)
print(factorial)
