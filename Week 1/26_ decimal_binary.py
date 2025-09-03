# Q26. Convert a decimal number to binary using loops. 

num = int(input("Enter a decimal number: "))
binary = ""
while num > 0:
    binary = str(num % 2) + binary
    num //= 2
print("The binary equivalent is:", binary)
