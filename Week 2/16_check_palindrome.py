# 16. Create a function that checks whether a string is a palindrome. 

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

word = (str(input("Enter a string to check if it's a palindrome: ")))
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")