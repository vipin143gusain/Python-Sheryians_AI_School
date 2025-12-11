#****************************************************************************************************************
"""LOOPS STARTS"""

#For Loops
a = range(1,21,1)
# for i in a : print(i)

# for i in range(21,1,-1): print(i) # reverse loop

# for i in range(-3,-16,-1): print(i) # minus reverse loop

#Table of 5
# n = int(input('Enter the number - '))
# for i in range(1,11): print(f'{n} * {i} = {n*i}')


# Loops for String

# name = "Vipin"
# for i in name: print(i)

# name = "Meena"
# for i in range(len(name)) : print(name[i])


# Break and Continue
#break
# for i in range(1,11):
#   if i == 5 : break

#   else : print('Break =',i)  


  #break
# for i in range(1,11):
#   if i == 5 : continue

#   else : print('Continue =',i) 



#   For Loop questions

# • Accept an integer and Print hello world n times.
# integer1 = int(input('Enter the number :- '))
# for i in range(integer1) : 
#   print('hello world')


# • Print natural number up to n.
# n = int(input('Enter natural numbers:-'))
# for i in range(1,n+1): 
#   print('These are nutural numbers =',i)


# • Reverse for loop. Print n to 1.

# rev = int(input('Enter the number'))

# for i in range(rev,-1+1,-1): print(i)


# • Take a number as input and print its table.
# table = int(input('Enter the number please - '))

# for i in range(1,11) :
#   print(table *i)
  # print(i)
  # print(f'{table} x {i} = {table*i}')


# • Sum up to n terms.
# n = int(input('Enter number: '))
# total = 0

# for i in range(1, n + 1):
#     prev = total
#     total = total + i
#     print(f'{prev} + {i} = {total}')

# print(f'Total sum is {total}')




# • Factorial of a number.

# f = int(input('Enter the Number please = '))

# fact = 1
# for i in range(1, f+1) :
#     prev = fact
#     fact *= i
#     print(f'{prev} * {i} = {fact}')

# print("Factorial", fact)
    


# • Print the sum of all even & odd numbers in a range separately.
# num_input = input("Enter the number = ")

# if not num_input.isdigit():
#     print(f"Invalid input! Only positive numbers allowed = {num_input}")
# else:
#     num = int(num_input)
#     total = 0

#     if num % 2 == 0:
#         for i in range(1, num + 1):
#             prev = total
#             print(f"{prev} + {i} = {prev + i}")
#             total += i
#         print(f"Total sum of Even Number is = {total}")

#     elif num % 2 == 1:
#         for i in range(1, num + 1):
#             prev = total
#             print(f"{prev} + {i} = {prev + i}")
#             total += i
#         print(f"Total sum of Odd Number is = {total}")        



# • Print all the factors of a number.
# n = int(input('Enter the factorial number - '))

# for i in range(1, n+1) :
#     if n%i == 0 : print(i)



# • Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 = 6

# perfectNumber = int(input('check the perfect number - '))
# sum = 0
# for i in range(1,perfectNumber):
#     if perfectNumber% i == 0 :
#        sum=sum + i
      
# if sum == i : print(f'{perfectNumber} is the perfect number') 
# else:   print(f'{sum} is the not perfect number') 


   

# • Check wether the number is prime or not.

# primeNumber = int(input('Write the Prime Number - '))

# count = 0
# for i in range(1, primeNumber+1):
#     if primeNumber % i == 0 : 
#         count = count + 1

# if count == 2 : 
#     print(f'{primeNumber} is the prime number')
# else:   print(f'{primeNumber} is not the prime number')   



# • Reverse a string without using in build functions. 

# reverseStr = input('Reverse a string : - ')

# # print(reverseStr[::-1]) - #This is one method
# revFinal = ''
# for i in range(len(reverseStr)-1,-1,-1) : 
#   revFinal = revFinal + reverseStr[i]
# print(revFinal)



 


# • Check string is Palindrome or not

name = "MAM"

emptyString = ""
for i in range(len(name)-1,-1,-1) :
  emptyString = emptyString + name[i]

if emptyString == name : print('This is a Palindrome')
else : print('This is not a Palindrome')



"""LOOPS Ends"""
#****************************************************************************************************************

