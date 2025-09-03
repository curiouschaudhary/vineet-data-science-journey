# 17. Write a function to count vowels in a string. 

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for c in s if c in vowels)

word = (str(input("Enter a string to count the vowels: ")))
print(f"The number of vowels in '{word}' is: {count_vowels(word)}")
