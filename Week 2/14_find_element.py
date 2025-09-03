# Q14. Write a function to find common elements in two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def find_common_elements(list1, list2):
    return [x for x in list1 if x in list2]

print("Common elements:", find_common_elements(list1, list2))
