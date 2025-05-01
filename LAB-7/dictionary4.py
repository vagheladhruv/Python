'''
4.	Write a program that reads a string from the keyboard and 
creates dictionary containing frequency of each character occurring in the string. 
'''
def frequency(string):
    freq = {}
    
    for char in string:
        if char in freq:
            freq[char] += 1  
        else:
            freq[char] = 1  
    return freq
string = input("Enter a string: ")

freq = frequency(string)

print("Character frequency:")
for char, freq in freq.items():
    print(f"'{char}': {freq}")
