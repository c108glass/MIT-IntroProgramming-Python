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

##Lecture 4 continued in next file
