# Function to calculate the area of a triangle

# Taking input from the user
height = float(input("Enter the height of the triangle: "))
length = float(input("Enter the base length of the triangle: "))

# Calculating the area
area = (height * length) / 2

# Displaying the result
print("Entered height value of triangle : ",height,)
print("Entered length value of triangle : ",length,)

print("The area of the triangle is = {}".format(area))
