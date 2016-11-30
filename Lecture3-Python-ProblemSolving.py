##Lecture 3
##Problem Solving
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Decrementing function: guaranteed to always terminate loop if:
##1.Map set of program variables to an integer.
##2.Starts with a non-negative value
##3.When <= 0, loop terminates.
##4.Decreased each iteration

##Find the cube root of a perfect cube #2. 
##Exhaustive Enumeration (Brute Force) - exhaust the space of all possible answers.
x = int(raw_input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)

##Approximation(using an epsilon). Find square root using Exhaustive Enumerationx
##These two programs do not work for finding exact square, only an approximation.
##The purpose is to show how program execution time is based on
##size of input, level of accuracy(epsilon), and size of iteration increment.
##More specifically, it is based on the algorithm used. 
x = 12345
epsilon = 0.01
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += 0.00001
    numGuesses += 1
print 'numGuesses =', numGuesses
if abs(ans**2 - x) >= epsilon:
    print 'Failed on square root of ', x
else:
    print ans, 'is close to square root of', x

##Here's a faster way. Bisection Search.
##Cut search space in half each iteration.
##This method takes 26 guesses for x = 12345. Previous algorithm took more than 11 million guesses.
x = 12345
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    #print low, high, ans
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x
##Can estimate the number of guesses by (x/epsilon)**2.
##Estimating number of guesses is useful for determining an appropriate algorithm,
##so that the program runs in a reasonable timeframe.
