# Student Grade Tracker - Kris, 2025
# This program lets the user enter student names and grades,
# stores the data in lists, then prints out all results and the class average.

# Create empty lists to hold student names and grades
student_names = []
student_grades = []

# Ask the user how many students they'll enter
num_students = int(input("How many students? "))

# Loop for each student to collect name and grade
for i in range(num_students):
    name = input("Enter student name: ")  # Get student name from user
    grade = float(input("Enter student grade: "))  # Get grade (make sure it's a number)
    student_names.append(name)  # Store name in list
    student_grades.append(grade)  # Store grade in list

# Print out all student names with their scores
print("\nAll results:")
for i in range(num_students):
    print(student_names[i], "scored", student_grades[i])

# Calculate the class average by adding all grades and dividing by the number of students
average = sum(student_grades) / num_students

# Print the class average
print("Class average is:", average)
