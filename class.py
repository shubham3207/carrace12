def add(a,b):
    print('function start')
    c=a+b
    print(c)
    print('funtion end')

    print('main start')
    print('function is calling')
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    ans= add(a,b)
    print('the sum is",ans')
    print('program end')

##function with no value and nol parameters

def sum():
    a=int(input("enter the first num"))
    b=int(input("enter the second num"))
    print(f"the sum of {a} and {b} is {a+b}")

sum()

###functions having parameters and no return type

def sum(a,b):
    print(f"the sum of {a} and {b} is {a+b}")

    sum(4,5)

###functions having no parameter and with return type
def sum():
    a=int(input("enter first number"))
    b=int(input("enter the second num"))
    return a+b

c=sum()
print(c)

###functiolns having parameters and return types
def sum(x,y):
    return x+y

a=int(input("enter first number"))
b=int(input("enter second number"))
c=sum(2,3)