# Write a program to count the number of digits in an integer.
num = int(input("Enter an integer: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("The number of digits is:", count)
