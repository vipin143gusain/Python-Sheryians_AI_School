import builtins

# Single Line Comment
print('Hello python')

""""This is multi line comments"""


#Variables

name = "Vipin"


#Case Sensitive
vipinGusain = "Vipin" #camelCase
VipinGusain = "Vipin" #PascalCase
vipin_gusain = "Vipin" #snake_case


#Data Types - Integers types
# 1,2,3, ... # natural numbers
# 0,1,2,3, ... # whole numbers
# -3, -2, -1, 0, 1, 2, 3 # integer numbers
# 1.5 #float numbers
# 10/2 #fraction numbers

a = 12
print(type(a)) 

#Complex Data Types
v=34j #complex data type


#Data Types - Strings
str = "Vipin 0906/1987 @&*()"
print(type(str))

num = 'a'
num2 =65
print(ord(num)) #with the help of ord you can check unicode of the characters

print(chr(num2)) #with the help of chr you can covert unicode to character 


""""Indexing of string"""

name = "Aaira"
print(name[2])


""""String Slicing"""

Fname = "Vipin Gusain"

print(Fname[6:12:1]) #starting point:, stop point: : how many slice you want to do


# DataType Type Conversion

a = 50
# Use builtins.str instead of the corrupted str()
a = builtins.str(a) 
print(type(a))




#Data Types - Boolean

#Falsy values => false, 0, "", 0.0, [], {}, ()
bol = ""
print(bool(bol)) #false 


positiveValue = 12
print(bool(positiveValue)) #true 





