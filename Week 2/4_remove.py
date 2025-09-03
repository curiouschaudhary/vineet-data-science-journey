# 4. Create a program that removes duplicates from a list. 

# l = [1, 2, 2, 3, 4, 4, 5]
# l = list(set(l))
# print(f"The list after removing duplicates is: {l}")



# 4. Create a program that removes duplicates from a list (order-preserving)

l = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

print("Original list:", l)
print("List after removing duplicates:", remove_duplicates(l))
