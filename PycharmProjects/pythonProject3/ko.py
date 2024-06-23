"""
# Get the number of students
num_students = int(input("Enter the number of students: "))

# Initialize lists to store student IDs, names, marks, and average marks
student_ids = [0]*num_students
student_names = []
student_marks = [[0]*3 for _ in range(num_students)]  # Assuming 3 courses per student
average_marks = []

# Collect information for each student
for i in range(num_students):
    # Get student ID and name
    student_ids[i] = int(input(f"Enter the ID for student {i+1}: "))
    student_names.append(input(f"Enter the name for student {i+1}: "))

    # Get marks for each course and calculate average mark
    total_marks = 0.0
    for j in range(3):  # Assuming 3 courses per student
        mark = float(input(f"Enter mark for course {j+1} for student {i+1}: "))
        student_marks[i][j] = mark
        total_marks += mark
    average_marks.append(total_marks / 3)  # Assuming 3 courses per student

from tabulate import tabulate

# Build the table
table = []
for i in range(num_students):
    row = [student_ids[i], student_names[i], average_marks[i]]
    table.append(row)

# Define the headers
headers = ["Student ID", "Student Name", "Average Mark"]

# Print the table
print(tabulate(table, headers=headers, tablefmt="grid"))
"""




