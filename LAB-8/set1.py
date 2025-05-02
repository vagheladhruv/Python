'''
1.	Write a program that converts words present in a list into uppercase and stores them in a set
'''

def word_to_upper(string):
    string_set=set()

    for i in string:
        string_set.add(i.upper())

    return string_set

string=["Devansh","Prince","abcd","efgh","IJKL","MNOP"]
print(f"Set of words in uppercase are {word_to_upper(string)}")
