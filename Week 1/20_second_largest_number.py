a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter one more number: "))
if a > b and a > c:
    second_largest = max(b, c)
elif b > a and b > c:
    second_largest = max(a, c)
else:
    second_largest = max(a, b)
print("The second largest number is:", second_largest)
