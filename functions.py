#****************************************************************************************************************
"""FUNCTIONS STARTS"""

# Function questions
def name () : print('Hello guys')
name()


#Parameters and Arguments - These are called positional arguments
def sum (a,b) : print(a+b)
sum(10,10)


#Types Of Arguments

#default argument and also called key word argument
def hello(name, age):print(f'hello {name} and your age is {age}')
hello(name='Vipin', age ='33')


#key word argument
def sub(a,b=5): print(a-b)
sub(10,3)

#Make a palindrome function

def palindrome(str):
  print('str',str)
  rev = ""
  for i in range(len(str)-1,-1,-1) :
    rev = rev + str[i]
    print('rev',rev)

  if rev == str : print(f'{str} is a palindrome')
  else: print(f'{str} is not a palindrome')



palindrome('NAMAN')
palindrome('RAMAN')


  




#****************************************************************************************************************
"""FUNCTIONS ENDS"""