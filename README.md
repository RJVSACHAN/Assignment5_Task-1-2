# Assignment5_Task-1-2
#ASSIGNMENT 5: Module 6: Data Structures and Strings in Python
# Task 1: Create a Dictionary of Student Marks

Marks = {'Joe':'78','Sam':'56', 'Rim':'91', 'Joy':'88'}
Student_Name = input("Enter the student's name: ")
if Student_Name in Marks:
    print(f"{Student_Name}'s marks: {Marks[Student_Name]}")
else:
    print(f"Student not found.")

#Task 2: Demonstrate List Slicing
Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Num)
print(Num[0:5])
print(reversed(Num[0:5]))
print(list(reversed(Num[0:5])))
