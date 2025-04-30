'''
2.	A list contains tuples containing roll no., name and age of student.
 Write a python program to create three lists separately for roll no., name and age
'''


students = [(101, "Keyur", 20), (102, "Dax", 22), (103, "Rohan", 19)]
roll_no = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]
print(f"Roll Numbers: {roll_no}")
print(f"Names: {names}")
print(f"Ages: {ages}")
