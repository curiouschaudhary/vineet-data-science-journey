# 22. Write a function to check if a string is an anagram. 

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

word1 = (str(input("Enter the first string: ")))
word2 = (str(input("Enter the second string: ")))
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
