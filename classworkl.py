def add():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    print(c)

    add()

### functions with parameters and no return value
def mul():
    a=int(input("enter first num"))
    b=int(input("enter second number"))
    c=a*b
    return c
prod=mul()
print(prod)

###function having parameter and return valule
def div(a,b):
    return a/b
a=int(input("enter first number"))
b=int(input("enter second number"))
c=div(a,b)
print(c)
###function having parameters and no return value
def sub(a,b):
    c=a-b
    print(c)
a=int(input("enter first number"))
b=int(input("enter second number"))
print(c)

