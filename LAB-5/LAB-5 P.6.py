# Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees

# Step 1: Define a list of temperatures in Fahrenheit
fahrenheit_temperatures = [32, 68, 77, 104, 212]
print("Temperatures in Fahrenheit:", fahrenheit_temperatures)

# Step 2: Convert each temperature to Celsius
celsius_temperatures = [(temp - 32) * 5 / 9 for temp in fahrenheit_temperatures]
print("Equivalent temperatures in Celsius:", celsius_temperatures)
