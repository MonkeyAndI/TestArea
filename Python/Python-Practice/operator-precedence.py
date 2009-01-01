#########################
## operator precedence 
#########################

# Assignment expression
print(donkey := True)
print(type(donkey))

# Lambda expression : Supports single line statements that returns some value.

##
x = lambda a : a + 10
print(x(5)) 

# lambda returns a function object
str1 = 'GeeksforGeeks'
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

##
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

##
def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y

# using function defined
# using def keyword : any number of lines inside a function block
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))

##
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
 
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())
	
##
# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))

## Nested Lambda
List = [[2,3,4],[1, 4, 164, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
print (  sorted([[2,3,14],[1, 2, 16, 6]]))
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-1] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)

##
#Filter out all odd numbers using filter() and lambda function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

#Filter all people having age more than 18, using lambda and filter() function
# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)


#Transform all elements of a list to upper case using lambda and map() function
# Python program to demonstrate use of lambda() function with map() function

animals = ['dog', 'cat', 'parrot', 'rabbit']
 
uppered_animals = list(map(lambda animal: animal.upper(), animals))
 
print(uppered_animals)

# Sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

#Find the maximum element in a list using lambda and reduce() function
import functools

lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))



################################
# if else
# where the block contains only a single line statement. 
# Instead of writing a block after the colon, we can write a 
# statement immediately after the colon.
number = 6
if number > 5:
	# Calculate square
	print(number**2)
	print(number**5)
	print(number*number)
	print(pow(number,2))
print('Next lines of code')

num1 = 0 #int(input('Enter first number '))
num2 = 3 #int(input('Enter second number '))

if num1 == num2:
	print(num1, 'and', num2, 'are equal')
elif num1 < 0:
	print(num1, "is less than zero")
elif num2 < 0:
	print(num2, "is less than zero")
else:	
	if num1 >= num2:print(num1, 'is greater than', num2)
	else:print(num1, 'is smaller than', num2)

x = 1
while x <= 5: print(x,end=" "); x = x+1;x=x+2

num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print("Sum of first 10 number is:", sum)

print("--")
num = 10
sum = 0
i = 1
while i <= num: sum = sum + i;i = i + 1;print("Sum of first 10 number is:", sum)

for num in range(10):
    if num > 5:
        print("Stop processing.")
        break
    print(num)
	
for num in range(3, 8):
    if num == 5:
        continue
    else:
        print(num)
		
		
#################################
# Boolean OR AND NOT
# Python Uses short-circuit evaluation, or lazy evaluation. 
# In other words, Python evaluates the operand on the RIGHT
# only when it needs to.
# Avoid lazy evaluation in a specific Boolean expression. 
# You can do so by using the bitwise operators (&, |, ~)
######

print(5 > 3 and 5 == 3 + 2)
print(5 < 3 and 5 == 5)
print(5 == 5 and 5 != 5)
print( 5 < 3 and 5 != 5)
		

def true_func():
	print("Running true_func()")
	return True
	

def false_func():
	print("Running false_func()")
	return False		
	
print(true_func() and false_func())  # Case 1
print(false_func() and true_func() ) # Case 2
print(false_func() and false_func())  # Case 3
print(true_func() and true_func() ) # Case 4
print( false_func() & true_func()) # Case 5

# By default, an object is considered true unless its class defines 
# either a __bool__() method that returns False or
# a __len__() method that returns zero, when called with the object
#built-in objects considered false:
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)

print ("77777777777777")
print(5 and 0.0)
print([] and 3)
print(0 and {})
print(3 and "")
print(False and "")

print ("888888888888888")
print( 2 < 4 and 2) ## (2 < 4) is an expression, 2 is an object
print( 2 and 2 < 4)
print( 2 < 4 and [])
print( [] and 2 < 4)
print( 5 > 10 and {})
print( {} and 5 > 10)
print( 5 > 10 and 4)
print( 4 and 5 > 10)
 
print ("99999999999999999999") 
#  the or operator stops once it finds a true operand
print( 5 or 2 and 2 < 1)
print((5 or 3) and 2 > 1)

print ("0000000000000000000000")
print( 0 < 5 < 10)
print( 0 < 25 < 10)

print ("-----------------------")
x = 5
y = 15
print(0 < x < 10 < y < 20)
# Equivalent and expression
print( 0 < x and x < 10 and 10 < y and y < 20)
print ("=====================")
a = 2
b = 4
c = 4
d = 4
if(not(a == b) and (c == d)):
   print("If Executed")
else:
   print("Else Executed")