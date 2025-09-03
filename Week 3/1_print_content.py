# Q1. Write a Python script to read a file and print its contents. 

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
