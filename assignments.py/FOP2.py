n=int(input("enter the number for factorial:"))
if n<0:
    print("the factorial is not valid")
elif n==0:
    print("factorial of 0 is :0 ")
else:
    multi=1
    for i in range(n,1,-1):
        multi*=i
    print("the factorial of the num is :",multi)
