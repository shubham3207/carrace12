###wap to print multiplication table of a given number using function
def mul(a):
    for i in range(1,11):
        print(a,"*",i,"=",a*i)

a=int(input("enter the number"))
mul(a)
