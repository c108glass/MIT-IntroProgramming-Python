##Lecture 4
##Machine Interpretation of a Program
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##One issue with the previous lecture's bisection search program (shown below)
##is that it doesn't account for an x less than 1.
##The square root of any x less than 1 will be greater than x.
##Therefore the bisection search region does not contain the answer.
##e.g. low = 0, high = .5, square root of .5 is approximately .75
##Running the below program with x less than 1 will eventually result in an endless loop. (Ctrl+C to stop)
x = .5
epsilon = 0.01
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print 'ans =', ans, 'low =', low, 'high =', high
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ans, 'is close to square root of', x

##So the code must be changed.
##The method Max() will choose the largest of its arguments.
##Setting high to max(x, 1.0) will ensure any x less than 1 will still be within range.
x = .5
epsilon = 0.01
low = 0.0
high = max(x, 1.0)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print 'ans =', ans, 'low =', low, 'high =', high
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ans, 'is close to square root of', x

##Functions(name, parameters, body) - allow me to use less code to do more. Decompostiton and Abstraction.
##Decomposition - Create structure. Self contained, reusable modules. Abstraction - Suppress detail.
##Def is used to define the function name.
##Return is used to give the function a value. Otherwise it will produce NONE when called.
def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
        returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon

##Can print the return value of the function or store it in a variable.
print withinEpsilon(2,3,1)
val = withinEpsilon(2,3,0.5)
print val

##Below will print x = 4, z = 4, x = 3. 
##This shows how the x in the function f(x) is not the same as the variable x = 3.
##When a function is called the formed parameter, x, is bound to the value of the actual parameter.
##Upon entry of a function, a new scope is created. Scope - mapping from names to objects.
##Each scope is a stackframe.
def f(x):
    x = x + 1
    print 'x =', x
    return x

x = 3
z = f(x)
print 'z =', z
print 'x =', x

####Below begins with the main scope, which calls the f1 scope, then the g scope.
####Asserts check expressions. If false, program will stop. Good for debugging.
####The fuction g will give an assertion error. I can check the stack viewer to take a closer look.
##def f1(x):
##    def g():
##        x = 'abc'
##        assert False 
##    x = x + 1
##    print 'x =', x
##    g()
##    return x
##
##x = 3
##z = f1(x)

##Test an int for even or odd.
def isEven(i):
    """assumes i a positive int
        returns True if i is even, otherwise False"""
    return i%2 == 0
            
##Strings - Non-scalar values.
##Below will sum the values in the string.
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits

##Tuple. Non-scalar data type. Can hold multiple elements of various types such as numbers or strings.
##When using two parameters in a range, the first is inclusive, the second is exclusive.
##Below prints the divisors of 100.
##The lone comma here (i,) makes it a tuple with one element instead of just an int. 
x = 100
divisors = ()
print divisors
for i in range(1, x):
    if x%i == 0:
        divisors = divisors + (i,)
        print divisors

print divisors ##(1, 2, 4, 5, 10, 20, 25, 50)
print divisors[0] + divisors[1] ##1 + 2 = 3
print divisors[2:4] ##4, 5, 10 but the last is exclusive so we get (4, 5)

##help() can be used in the shell to find syntax info on a built-in function. (e.g. help(range))
