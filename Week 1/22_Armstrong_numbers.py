# Q22. Create a program to print all Armstrong numbers between 1 to 1000. 

for num in range(1, 1001):
    order = len(str(num))
    sum = 0
    temp = num
    while temp != 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if sum == num:
        print(num)
