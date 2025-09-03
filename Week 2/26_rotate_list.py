# 26. Create a function to rotate a list left by k positions. 

list = [1, 2, 3, 4, 5, 6, 7]

def rotate_list(lst, k):
    k = k % len(lst)  # handle rotations greater than list length
    return lst[k:] + lst[:k]

print(rotate_list(list, 3))