# 23. Create a nested dictionary to represent student records. 
students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'courses': ['Math', 'Science']
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'courses': ['English', 'History']
    }
}
for student_id, info in students.items():
    print(f"ID: {student_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")



# student_id = input("Enter new student ID: ")
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# courses = input("Enter courses (comma-separated): ").split(",")

# students[student_id] = {
#     'name': name,
#     'age': age,
#     'courses': [course.strip() for course in courses]
# }
