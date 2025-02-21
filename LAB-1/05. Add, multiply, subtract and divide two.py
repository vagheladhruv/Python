# Add, multiply, subtract and divide two numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

# Addition
add=a+b

# Subtraction
sub=a-b

# Multiplication
mul=a*b

# Division

if b!=0:
    div=a/b
else:
    print("Error: Division by zero is not allowed.")
    div=None

print("Addition of",a,"and",b,"is",add,)

print("Subtraction of",a,"and",b,"is",sub)

print("Multiplication of",a,"and",b,"is",mul)

if div is not None:
    print("Division of",a,"and",b,"is",div)




