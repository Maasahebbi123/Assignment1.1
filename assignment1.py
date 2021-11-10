#Let's play with Fibonacci.
n=int(input("enter number of terms:"))
if n<=0:
    print("invalid number")
if n==1:
    print(0)
if n>=2:
    a=0
    b=1
    print(1,end=" ")
    for i in range (2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        

