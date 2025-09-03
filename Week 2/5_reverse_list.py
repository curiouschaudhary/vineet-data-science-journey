# 5. Write a function to reverse a list. 

l = [1, 2, 3, 4, 5]
def reverse_list(lst):
    return lst[::-1]

reversed_l = reverse_list(l)
print(f"The reversed list is: {reversed_l}")
