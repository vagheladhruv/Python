# Calculate interest where I = PRN/100.


# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calculating interest
interest = (principal * rate * time) / 100

# Displaying the result
print("The interest for a principal amount of {} at a rate of {}% for {} years is {}".format(principal, rate, time, interest))
