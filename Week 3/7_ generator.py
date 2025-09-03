# Q7. Write a generator that yields even numbers up to N. 

def even_number_generator(N):
    for num in range(N + 1):
        if num % 2 == 0:
            yield num

N = 100
print(list(even_number_generator(N)))