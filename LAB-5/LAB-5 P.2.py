''''Generate 20 random integers and store them in a list. Accept a number
from the user and print position of all occurrences of that number in the list.'''

import random

# Generate 20 random integers and store them in a list
random_integers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of random integers:", random_integers)

# Accept a number from the user
user_number = int(input("Enter a number to find its positions in the list: "))

# Find positions of all occurrences of the number
positions = [index for index, value in enumerate(random_integers) if value == user_number]

# Print the positions
if positions:
    print(f"The number {user_number} occurs at positions:", positions)
else:
    print(f"The number {user_number} does not occur in the list.")
