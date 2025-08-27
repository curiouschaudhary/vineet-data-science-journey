# Q29. Create a program to check whether a number is prime or not. 

num = int(input("Enter a positive integer: "))
is_prime = True

if num == 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
