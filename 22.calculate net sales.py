# Function to calculate net sales


# Taking input from the user
gross_sales = float(input("Enter the gross sales: "))

# Calculating net sales
discount = gross_sales * 0.10  # 10% of gross sales
net_sales = gross_sales - discount

# Displaying the result
print("The net sales is {}".format(net_sales))
