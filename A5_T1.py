# Task 1: Create a Dictionary of Student Marks

Marks = {'Joe':'78','Sam':'56', 'Rim':'91', 'Joy':'88'}
Student_Name = input("Enter the student's name: ")
if Student_Name in Marks:
    print(f"{Student_Name}'s marks: {Marks[Student_Name]}")
else:
    print(f"Student not found.")