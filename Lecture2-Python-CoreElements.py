##Lecture 2
##Core Elements Of A Program
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Variable-assignment binds name to object.
x = 3
x = x*x
print x 

##Raw input-always interprets user input as a string.
##Adding 'float' before the 'raw_input' will change the output type.
y = float(raw_input('Enter a number: '))
print y
print type(y)

y = (raw_input('Enter a number: '))
print y
print type(y)

##Using conditional statements 'if-else-elif'.
##'%' is a remainder or mod operator.
##'==' is used for comparision, '=' is used for assignment.
##Indentation is very important in Python (no brackets). Below is an example of nesting conditionals.
x = int(raw_input('Enter an integer: '))
if x%2 == 0: 
    print 'The Integer is Even'
else:
    print 'The Integer is Odd'
    if x%3 != 0: ##This indent nests the 'if' condition within the 'else' condition
        print 'and not divisible by 3'

##Iteration. Find the cube root of a perfect cube.
##The 'while' loop steps through integers one at a time starting with 0,
##until it equals or exceeds the absolute value of x.
##Then ans is checked to see if it is a perfect cube of x.
##The absolute value of x is needed to prevent an endless while loop when a negative x is used.
##Finally, if a negative x was used, then ans will also need to be converted to negative. (e.g. perfect cube of -27 is -3) 
x = int(raw_input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    
if ans*ans*ans != abs(x):
    print x, ' is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
