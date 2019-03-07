num = int(input("Enter the number " ))
factorial = 1

if num < 0:
    print("Factorial for negative does not exsits")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial *= i
    print("the factorial of",num,"is",factorial)

#factorial USING recursion
def rec_factorial(n):
    if n==1:
        return n
    else:
        return n*rec_factorial(n-1)

num = int(input("enter the fatorial "))

if num < 0:
    print("does not exist for negative numbers")
else:
    print("the factorial of",num,"is",rec_factorial(num))
        