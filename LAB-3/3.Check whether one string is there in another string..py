# Accept two strings. Check whether one string is there in another string.

def check_string_in_another(string1, string2):
    return string1 in string2

# Test the function

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


if check_string_in_another(string2, string1):
        print(f"{string2} is found in {string1}")
else:
        print(f"{string2} is not found in {string1}")
