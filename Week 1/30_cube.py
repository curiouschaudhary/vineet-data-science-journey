# Q30. Write a program to display the cube of the number up to an integer. 

num = int(input("Enter an integer: "))
for i in range(1, num + 1):
    print("The cube of", i, "is", i ** 3)
