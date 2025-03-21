# Write a function that removes one string from another string, if present
# Function to remove one string from another
def remove_substring(main_string, substring):
    result = ""
    i = 0
    while i < len(main_string):
        # Check if the substring exists starting from the current index
        if main_string[i:i+len(substring)] == substring:
            # Skip the length of the substring
            i += len(substring)
        else:
            # Add the current character to the result
            result += main_string[i]
            i += 1
    return result

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring to remove: ")

# Call the function and display the result
result = remove_substring(main_string, substring)
print("Resulting string:", result)


# Example usage
'''main_string = "abcdef"
substrating = "cd"
final_string = remove_substring(main_string, substrating)

print("Final string:", final_string) '''



