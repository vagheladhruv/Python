'''Generate 30 random numbers and put them in a list.
Create two more lists – one containing only +ve numbers and another with –ve nos.'''


import random

# Step 1: Generate 30 random numbers in the range -50 to 50 and store them in a list
random_numbers = [random.randint(-50, 50) for _ in range(30)]
print("Generated list of random numbers:", random_numbers)

# Step 2: Create a list of positive numbers
positive_numbers = [num for num in random_numbers if num > 0]

# Step 3: Create a list of negative numbers
negative_numbers = [num for num in random_numbers if num < 0]

# Step 4: Print the lists
print("List of positive numbers:", positive_numbers)
print("List of negative numbers:", negative_numbers)
