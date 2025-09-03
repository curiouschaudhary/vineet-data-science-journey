str = input("Enter a string: ")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print("Number of vowels in the string:", count_vowels(str))
