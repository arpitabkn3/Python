num=int(input("enter the number"))
fact=1
if num<0:
    print("factorial does not exist")
if num==0:
    print("factroial of 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
        print("factorial of the number is",fact)
