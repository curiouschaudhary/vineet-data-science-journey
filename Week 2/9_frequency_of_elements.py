#  9. Write a function to count the frequency of elements in a list. 

l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 5]

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print("Original list:", l)
print("Frequency of elements:", count_frequency(l))
