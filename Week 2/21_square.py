# 21. Create a list comprehension to get squares of all even numbers in a range. 

squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
for x in range(10):
    if x % 2 == 0:
        print("square of", x, "is", x**2)
