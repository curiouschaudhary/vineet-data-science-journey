# 19. Write a function to remove all punctuation from a string. 

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

word = (str(input("Enter a string to remove punctuation: ")))
print(f"The string without punctuation is: '{remove_punctuation(word)}'")