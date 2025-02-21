#Calculate area & perimeter of a rectangle.


# Taking input from the user
length = float(input("Enter the length of the rectangle in cm: "))
breadth = float(input("Enter the breadth of the rectangle in cm: "))

# Calculating area and perimeter
area= length * breadth
perimeter= 2 * (length + breadth)

# Displaying the results
print("The area of the rectangle is {} square cm".format(area))
print("The perimeter of the rectangle is {} cm".format(perimeter))
