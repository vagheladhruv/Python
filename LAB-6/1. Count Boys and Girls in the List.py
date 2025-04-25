'''1.	A list contains names of boys and girls as its elements.
Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))'''


names = [("Dhruv", "Darsh"), "Pragati", "Priyanshi", ("Jainesh", "Aarav"), "Krupali"]
boys_count = sum(isinstance(ele, tuple) for ele in names)
girls_count = len(names) - boys_count
print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
