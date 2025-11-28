"""COMMENTS STARTS"""

#Single Line Comments -> use # for the single line comments
print('Hello Vipin')

#Multi Line Comments -> use """ """ for the Multi line comments
"""My Name is vipin ~
my age is 38 years old"""

"""COMMENTS ENDS"""

#****************************************************************************************************************

"""VARIABLES STARTS"""

name = "Vipin"

#Case Sensitive
vipinGusain = "Vipin" #camelCase
VipinGusain = "Vipin" #PascalCase
vipin_gusain = "Vipin" #snake_case

"""VARIABLES ENDS"""

#****************************************************************************************************************


"""DATA TYPES STARTS"""
#1. Integers (Numbers) - - First Data Type
# 1,2,3, ... #natural numbers
# 0,1,2,3, ... #whole numbers
# -3, -2, -1, 0, 1, 2, 3 #integer numbers
# 1.5 #float numbers
# 10/2 #fraction numbers

a = 12
print(type(a))

#Complex Data Type (or iyota)
k = 10j  #just put j in the last of any digit its become complex data type
print(type(k))

#---------------------------------------------------------------------------------------------------------------

#2. String - Second Data Type
string = "asdfasd 343434 #$$%%##@@"
print(type(string))



#string unicode 
a = 'Q'
emoji = '🤪'
print('a unicode is', ord(a))
print('emoji unicode is', ord(emoji))

emojiUnicode = 129322
print('convert unicode to character', chr(emojiUnicode))


#String Indexing
animal = 'sher'
print('string indexing of 1 is =>',animal[1])
print('string negative indexing  of r is =>',animal[-1])

#String Slicing - #starting point:, stop point: : steps of our slicing

fName = "Vipin Kumar Gusain"
print('String Slicing method 1 = ',fName[12:18:1])
print('String Slicing method 2 = ',fName[6:11:])



#3. Boolean - Third Data Type
bol = True
bo2 = False
print('Boolean type is ', type(bol))


#DataType 4 Types of Conversion - int(), str(), float(), bool()

#int() to str()
num = 12
print("type of num = ", type(num))

num = str(num)
print("integer to string conversion = ", type(num))


#str() to int()
aa = "22"
aa = int(aa)

print('string to integer conversion = ', aa)


#int() to bool() 
b = 12
b=bool(b)
print('interger to boolean conversion = ', b)

#Falsy values => false, 0, "", 0.0, [], {}, ()
number = 0.0
print('falsy value of boolean is ',bool(number))



#There are 2 types of conversion - implicit and explicit 

"""DATA TYPES ENDS"""

#****************************************************************************************************************




"""INPUT AND OUTPUT STARTS"""
#We also use for output is print() function
first_name = "Vipin" 
age = 38
#how to write normal string
print('My name is',first_name,'.','And my age is',age)

#how to write formatted string
print(f'My name is {first_name }. And my age is {age}')


#Input
age = int(input('What is your age'))
full_name = input('What is your full name')

print(f'My name is {full_name} and my age is {age} yrs old')

print('type of age is = ',type(age))
print('type of full_name is = ',type(full_name))


"""INPUT AND OUTPUT ENDS"""

#****************************************************************************************************************









