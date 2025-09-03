# 30. Create a function to find unique elements present in only one of two lists. 

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def find_unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    return unique_to_list1, unique_to_list2

unique1, unique2 = find_unique_elements(list1, list2)
print("Unique to list1:", unique1)
print("Unique to list2:", unique2)