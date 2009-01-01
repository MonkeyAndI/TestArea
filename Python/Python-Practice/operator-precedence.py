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