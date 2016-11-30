##Lecture 4 (Continued)
##Machine Interpretation of a Program
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

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
##When a function is called: 1)The formed parameter, x, is bound to the value of the actual parameter.
##2)Upon entry of a function, a new scope is created. Scope - mapping from names to objects.
##Each scope is stackframe.
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

####
def findRoot(pwr, val, epsilon):
    """assumes pwr an int; val, epsilon floats
        pwr and epsilon > 0
        if it exists,
            returns a value within epsilon of val**pwr
            otherwise returns None"""
    assert type(pwr) == int and type(val) == float\
           and type(epsilon) == float
    assert pwr > 0 and epsilon > 0
    if isEven(pwr) and val < 0:
        return None
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/2.0
    while not withinEpsilon(ans**pwr, val, epsilon):
        print 'ans =', ans, 'low =', low, 'high =', high
        if ans**pwr < val:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

def testFindRoot():
    """x float, epsilon float, pwr positive int"""
    for x in (-1.0, 1.0, 3456.0):
        for pwr in (1, 2, 3):
            ans = findRoot(pwr, x, 0.001)
            if ans == None:
                print 'The answer is imaginary'
            else: print ans, 'to the power', pwr,'is close to', x
            
##Strings - Non-scalar values
##Below will sum the values in the string.
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits

##
x = 100
divisors = ()
print divisors
for i in range(1, x):
    if x%i == 0:
        divisors = divisors + (i,)
        print divisors

print divisors
print divisors[0] + divisors[1]
print divisors[2:4]
