num = int(input("Enter a number: "))
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print("Is the number a palindrome?", is_palindrome(num))
