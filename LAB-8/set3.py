'''
3.	Create an empty set. Write a program that adds five new names to this set, 
modifies one existing name and deletes two names from it.
'''

"""def add_modify_delete():

    names=set()
    names.update(["AAA","BBB","CCC","DDD","EEE"])

    print(names)
    names.discard("AAA")
    names.add("LLL")
    print(names)
    names.discard("DDD")
    names.discard("BBB")
    print(names)
    # names.add("AAA")
    # names.add("BBB")
    # names.add("CCC")
    # names.add("DDD")
    # names.add("EEE")

    # print(names)
    # for i in names:
    #     names.add(modify_string(i))
    #     names.discard(i)
    #     break

    # print(names)

    
    
    # print(names)

add_modify_delete()"""

# Create an empty set
names_set = set()

# Add five new names to the set
names_to_add = {"Dhruv", "Dax", "Tisha", "Ayushi", "Darsh"}
names_set.update(names_to_add)

# Modify one existing name: sets are unordered and elements are immutable,
# so we remove the old name and add the new one
names_set.remove("Ayush")
names_set.add("Shruti")

# Delete two names from the set
names_set.remove("Darsh")
names_set.remove("Ayushi")

# Print the final set
print(names_set)
