# Function to calculate net salary


# Taking input from the user
gross_salary = float(input("Enter the gross salary: "))

# Calculating net salary
allowance = gross_salary * 0.10  # 10% of gross salary
deduction = gross_salary * 0.03  # 3% of gross salary
net_salary = gross_salary + allowance - deduction
    
# Displaying the result
print("Entered gross salary : ",gross_salary, "Rs.")
print("Allowance : ",allowance, "Rs.")
print("Deduction : ",deduction, "Rs.")
print("The net salary is : {} Rs.".format(net_salary))
