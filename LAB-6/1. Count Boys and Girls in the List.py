names = [("John", "Peter"), "Sarah", "Emma", ("Mike", "Tom"), "Sophia"]
boys_count = sum(isinstance(ele, tuple) for ele in names)
girls_count = len(names) - boys_count
print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
