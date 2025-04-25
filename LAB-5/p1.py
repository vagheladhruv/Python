'''Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos.
Replace the third element of odd integers with  a list of 4 even integers.
Flattern, sort and print the list. Provide appropriate message at each stage.'''

'''import random

odd_integers = [ random.randint(range(1,100,2))  for _ in range(5) ]
print("List of 5 odd integers : ", odd_integers)

even_integers = [random.randint(range(2,100,2)) for _ in range(4)]
print("List of 4 even integers : ", even_integers)

odd_integers[2] = even_integers

print("List After replacing third element with even integers : ," , odd_integers)

#flat_list = [num for sublist in odd_integers for num in sublist]
#print("Flattern List :" , flat_list)

flatt_list = sum(odd_integers, [])
print("Flattern List :" , flatt_list)

flat_sorted_list = sorted(flatt_list)
print("Soarted List : " , flat_sorted_list)
'''



import random

# Step 1: Create a list of 5 random odd integers
odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("Generated list of odd integers:", odd_integers)

# Step 2: Create a list of 4 random even integers
even_integers = [random.choice(range(2, 101, 2)) for _ in range(4)]
print("Generated list of even integers:", even_integers)

# Step 3: Replace the third element of odd integers with the list of 4 even integers
odd_integers[2] = even_integers
print("List of odd integers after replacing the third element with even integers:", odd_integers)

# Step 4: Flatten the list
flattened_list = [item for sublist in odd_integers for item in (sublist if isinstance(sublist, list) else [sublist])]
print("Flattened list:", flattened_list)

# Step 5: Sort the flattened list
sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)
