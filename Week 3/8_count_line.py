# Q8. Create a program to count lines and words in a file. 

def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count
file_path = 'sample.txt'  # replace with your file path
line_count, word_count = count_lines_and_words(file_path)
print(f"Lines: {line_count}, Words: {word_count}")