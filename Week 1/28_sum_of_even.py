# Q27. Create a program to find the square root of a number. 

num = int(input("Enter an integer: "))
sum_even = 0
for i in range(2, num + 1, 2):
    sum_even += i
print("The sum of even numbers up to", num, "is", sum_even)
