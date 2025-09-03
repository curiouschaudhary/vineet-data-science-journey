# 20. Write a function to capitalize the first letter of each word in a string. 

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

word = (str(input("Enter a string to capitalize the first letter of each word: ")))
print(f"The capitalized string is: '{capitalize_words(word)}'")
