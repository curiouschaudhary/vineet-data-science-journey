# 29. Write a function to merge two dictionaries and handle key collisions by summing values. 

def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # start with dict1's keys and values
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value  # sum values for overlapping keys
    return merged

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print("Merged dictionary:", merge_dicts(dict1, dict2))
