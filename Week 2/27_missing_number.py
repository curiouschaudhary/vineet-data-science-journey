# 27. Write a function to find the missing number from a list of 1 to N. 

def find_missing_number(lst):
    n = len(lst) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum
list = [1, 2, 4, 5, 6]
print("List:", list)
print("Missing number:", find_missing_number(list))