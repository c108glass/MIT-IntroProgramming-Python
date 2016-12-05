##Lecture 8
##Efficiency and Order of Growth
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Efficiency is really about algorithms.
##When confronted with a problem, we should try to reduce to a previous solved problem.
##Computational Complexity. Focus on worse case.
##Find how the computation grows with respect to the size of input.
##Use a model of asymptotic growth. Big Oh. O(n), provides upper bound.
##O(1) -Constant, independant of input
##O(log n) - Logarithmic
##O(n) - Linear
##O(n log n) - Log Linear
##O(n**c) - Polynomical
##O(c**n) - Exponential
import pylab, math

def showGrowth(lower, upper):
    log = []
    linear = []
    quadratic = []
    logLinear = []
    exponential = []
    for n in range(lower, upper+1):
        log.append(math.log(n, 2))
        linear.append(n)
        logLinear.append(n*math.log(n, 2))
        quadratic.append(n**2)
        exponential.append(2**n)
    pylab.plot(log, label = 'log')
    pylab.plot(linear, label = 'linear')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(linear, label = 'linear')
    pylab.plot(logLinear, label = 'log linear')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(logLinear, label = 'log linear')
    pylab.plot(quadratic, label = 'quadratic')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(quadratic, label = 'quadratic')
    pylab.plot(exponential, label = 'exponential')
    pylab.legend(loc = 'upper left')
    pylab.figure()   
    pylab.plot(quadratic, label = 'quadratic')
    pylab.plot(exponential, label = 'exponential')
    pylab.semilogy()
    pylab.legend(loc = 'upper left')
    return

showGrowth(1, 1000)
pylab.show()


##def f(n):
##    assert n >= 0
##    answer = 1
##    while n > 1:
##        answer *= n
##        n -= 1
##    return answer
##
##def fact(n):
##    assert n >= 0
##    if n <= 1:
##        return n
##    else:
##        return n*fact(n - 1)
##
##def g(n):
##    x = 0
##    for i in range(n):
##        for j in range(n):
##            x += 1
##    return x
##
##def h(x):
##    assert type(x) == int and x >= 0
##    answer = 0
##    s = str(x)
##    for c in s:
##        answer += int(c)
##    return answer

