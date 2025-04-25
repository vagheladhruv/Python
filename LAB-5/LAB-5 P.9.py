""" 9.Take two lists of numbers. Create third list of numbers for only
those numbers from first list which are not there in 2nd list
(use list comprehension). """



# Step 1: Define two lists of numbers
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 8, 9]

# Step 2: Create a third list using list comprehension
list3 = [num for num in list1 if num not in list2]

# Step 3: Print the third list
print("Numbers from the first list that are not in the second list:", list3)
