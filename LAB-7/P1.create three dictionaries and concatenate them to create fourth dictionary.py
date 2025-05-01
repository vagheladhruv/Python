'''
Write a program to create three dictionaries and 
concatenate them to create fourth dictionary.
'''

a={'a1':"DAX",'a2':"Maitri",'a3':"Dhruv"}
b={1:"Shruti",2:"jenil",3:"Het"}
c={1:"Patel",2:"Borad",3:"Vaghela"}
d={**a,**b,**c}
print("COncatenated Dictinary:",d)
