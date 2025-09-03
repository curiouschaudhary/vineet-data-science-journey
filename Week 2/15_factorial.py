# 15. Write a function that returns the factorial of a number. 
n = int(input("Enter a number for factorial calculation: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"The factorial of {n} is: {factorial(n)}")