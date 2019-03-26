def rec_factorial(num):
    """Function to return the 
    factorial of the given number."""
    if num == 1:
        return 1
    else:
        return num*rec_factorial(num-1)

# print("the factorial of is",rec_factorial(5))
# num = int(input("Enter the number: "))
num = 8
if num < 0:
    print("factorial of negative number doesn't exist")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of", num,"is",rec_factorial(num))
    