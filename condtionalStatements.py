#****************************************************************************************************************
"""CONDITIONALS STATEMENTS STARTS"""

#IF ELSE 
# a=9
# if a>10 :
  # print(f'{a} is greater than 10')

#ELSE 
# else:
  #  print(f'{a} is less than 10')



#ELIF
# money = int(input('Enter the money = '))

# if(money == 10) : print(f'I will buy the ice-cream')
# elif(money == 20) : print(f'I will buy the cone ice-cream')
# else : print(f'I cannot buy the ice-cream')



#Exercise 

#Q1. Açcept two numbers and print the greatest between them.
# numberOne = int(input('Enter the first number'))
# numberTwo = int(input('Enter the second number'))

# if(numberOne > numberTwo) : print(f'numberOne = {numberOne} is greater than numberTwo = {numberTwo}')
# elif (numberTwo > numberOne): print(f'numberTwo = {numberTwo} is greater than numberOne = {numberOne}')
# else :  print(f'numberTwo = {numberTwo} equal as numberOne = {numberOne}')


#Q2. Accept the gender from the user as char and print the respective greeting message
#Ex - Good Morning Sir (on the basis of gender)

# gender = str(input('Enter your gender?'))

# if(gender == "male" or gender =='m'): print('Good Morning Sir')
# elif(gender == "female" or gender =='f'): print('Good Morning Madam')
# else : print('Wrong input. Please enter male or female only')



# Q3. Accept an integer and check whether it is even or odd.

# user_input = input("Enter the number only: ")

# Check if input is numeric
# if user_input.isdigit():  
#     integer = int(user_input)

#     if integer % 2 == 0:
#         print(f"{integer} is an even number")
#     else:
#         print(f"{integer} is an odd number")

# else:
#     print(f"'{user_input}' is not a valid number. Please enter digits only.")





#Q4. Accept name and age from the user. Check if the user is a valid voter or not.
#Ex- "hello shery you are a valid voter"

# name = input('Write your name?')
# age = int(input('What is your age?'))
# if(age < 18) : print(f'{name} you are not eligible to vote. You can vote age of 18 or above')
# elif age >= 18: print(f'{name} you are a valid voter')
# else :print(f'{name} you are not a valid voter')



#Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)
# year = int(input('Enter any year :-'))
# if year%4==0 or year%400 ==0 and year%100!=0: print(f'{year} is the leap year')
# else: print(f'{year} is not the leap year')




# If- elif ladder
#  You can also create if elif ladder using multiple conditions of
# elif.
# - For understanding solve this question
# - take the input of temperature in celsius.
# - Below 0°C - "Freezing Cold #"
# - 0°C to 10°C → "Very Cold
# - 10°C to 20°C → "Cold ""
# - 20°C to 30°C - "Pleasant
# - 30°C to 40°C → "Hot
# - Above 40°C → "Very Hot

temp = int(input('Enter the Temperature-'))

if temp > 0 and temp <= 10: print(f'Very Cold')
elif temp > 10 and temp <= 20: print(f'Cold')
elif temp > 20 and temp <= 30: print(f'Pleasant')
elif temp > 30 and temp <= 40: print(f'Hot')
elif temp > 40 : print(f'Very Hot')
else:  print(f'Freezing Cold')



"""CONDITIONALS STATEMENTS ENDS"""
#****************************************************************************************************************

