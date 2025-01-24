# Function to swap two values

# Taking input from the user
value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")

# Swapping the values
value1, value2 = value2, value1

# Displaying the result
print("Before swapping, the first value is '{}' and the second value is '{}'".format(value2, value1))

print("After swapping, the first value is '{}' and the second value is '{}'".format(value1, value2))
