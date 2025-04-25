'''Generate 50 random numbers in the range 1 and 30.
Remove all duplicate values from the list.'''



import random

# Generate 50 random numbers in the range 1 to 30
random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Generated list of random numbers:", random_numbers)

# Remove duplicates by converting the list to a set
unique_numbers = list(set(random_numbers))
print("List after removing duplicates:", unique_numbers)
