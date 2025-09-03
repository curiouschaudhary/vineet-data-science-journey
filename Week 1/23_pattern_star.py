# Write a Python program to print a pattern of stars in a triangle. 

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))