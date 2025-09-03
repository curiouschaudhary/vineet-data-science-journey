# Q4. Write a program to handle file not found error. 

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
