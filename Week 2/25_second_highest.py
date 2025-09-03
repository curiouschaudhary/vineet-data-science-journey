# 25. Write a program to find the second highest number in a list. 


def find_second_highest(numbers):
    # remove duplicates so same number doesn't count twice
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None  # no second highest
    
    # sort the list in ascending order
    unique_numbers.sort()
    
    # second highest will be the second last element
    return unique_numbers[-2]


num_list = [3, 1, 4, 4, 25, 5, 2]
print("Number list:", num_list)
print("Second highest number:", find_second_highest(num_list))
