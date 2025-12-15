#****************************************************************************************************************
"""WHILE LOOPS STARTS"""

# While loop questions
# • Separate each digit of a number and print it on the new line
# a = 2561

# while a > 0 :
#   print(a%10)
#   a = a // 10


# • Accept a number and print its reverse.

# b = 456
# rev = 0
# while b > 0 :
 
#   rev = rev * 10 + b % 10
#   print('rev', rev)
#   b = b // 10

# print (rev)


# • Accept a number and check if it is a palindromic number and its reverse are equal)

# b = 121
# copy = b
# rev = 0
# while b > 0 :
 
#   rev = rev * 10 + b % 10
#   # print('rev', rev)
#   b = b // 10

# if copy == rev: print('its a palindromic number')
# else :  print('its a not  palindromic number')



# • Create a random number guessing game with py
import random

num = random.randint(1,10)
print(num)
tries = 0

while True:

  guess = int(input('Enter the random number - '))

  if num == guess :
    tries +=1
    print(f'Your are the right and guessed the number in {tries} tries')
    break

  elif  guess > num : 
     tries +=1
     print('Go little higher')
  elif  guess < num: 
     tries +=1
     print('Go little smaller')

  else : print('Your number is not correct')





#****************************************************************************************************************
"""WHILE LOOPS ENDS"""