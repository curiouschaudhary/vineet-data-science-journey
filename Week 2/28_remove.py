# 28. Write a program to remove all None values from a list. 

def remove_none_values(lst):
    return [x for x in lst if x is not None]

list = [1, 2, None, 4, None, 5]
print("Original list:", list)
print("List after removing None values:", remove_none_values(list))