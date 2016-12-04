##Lecture 7
##Debugging
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Print statements can very useful for eliminating assumptions/debugging code.
##When in doubt, print the value to be sure. repr() is also useful to see exactly what's going on.

##Be careful to not test two floats to be equal.
##binary vs decimal. Python rounds to 17th digit. (binary representation of decimal 0.1 is infinite) 
print(0.1) ##0.1
print repr(0.1) ##0.10000000000000001

x = 0.0
numIters = 100000
for i in range(numIters):
    x += 0.1
print x #prints 10000.0, because print automatically rounds
print repr(x) #prints 10000.000000018848
print 10.0*x == numIters #False! 

##Instead do something like this to test if they are close enough:
def close(x, y, epsilon = 0.00001):
    return abs(x-y) < epsilon

if close(10.0*x, numIters):
    print 'Good enough'

##Test Harness - 
##code used for testing/debugging that isn't exactly required for the purpose of the program.
