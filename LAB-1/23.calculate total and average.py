# Function to calculate total and average


# Taking input from the user for three subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculating total and average
total = subject1 + subject2 + subject3
average = total / 3

# Displaying the results
print("The total marks are {}".format(total))
print("The average marks are {}".format(average))
