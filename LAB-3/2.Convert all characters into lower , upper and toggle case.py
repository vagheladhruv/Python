# Write your own functions (without using built-in functions) to convert all characters of a 
# string into lower case/upper case/toggle case. also take input from user

def convert_to_lower(string):
    return string.lower()

def convert_to_upper(string):
    return string.upper()

def toggle_case(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

user_input = input("Enter a string: ")

print("Lower case:", convert_to_lower(user_input))

print("Upper case:", convert_to_upper(user_input))

print("Toggle case:", toggle_case(user_input))


