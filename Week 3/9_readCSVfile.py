# Q9. Write a program to read a CSV file and print its contents. 

import csv

file_path = "netflix_titles_nov_2019.csv"

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"{header[0]:<12} {header[1]:<10} {header[2]:<40}")
    print("-" * 70)
    for row in reader:
        print(f"{row[0]:<12} {row[1]:<10} {row[2]:<40}")
