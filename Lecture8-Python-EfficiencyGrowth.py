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

##Examples below plot the differences.
##Basically we try not use anything more than logLinear algorithms. Quadratic is impractical. Exponential is ridiculous.
##However there is way to solve exponential problems by other means.
##import pylab, math
##
##def showGrowth(lower, upper):
##    log = []
##    linear = []
##    quadratic = []
##    logLinear = []
##    exponential = []
##    for n in range(lower, upper+1):
##        log.append(math.log(n, 2))
##        linear.append(n)
##        logLinear.append(n*math.log(n, 2))
##        quadratic.append(n**2) 
##        exponential.append(2**n) 
##    pylab.plot(log, label = 'log')
##    pylab.plot(linear, label = 'linear')
##    pylab.legend(loc = 'upper left')
##    pylab.figure()
##    pylab.plot(linear, label = 'linear')
##    pylab.plot(logLinear, label = 'log linear')
##    pylab.legend(loc = 'upper left')
##    pylab.figure()
##    pylab.plot(logLinear, label = 'log linear')
##    pylab.plot(quadratic, label = 'quadratic')
##    pylab.legend(loc = 'upper left')
##    pylab.figure()
##    pylab.plot(quadratic, label = 'quadratic')
##    pylab.plot(exponential, label = 'exponential')
##    pylab.legend(loc = 'upper left')
##    pylab.figure()   
##    pylab.plot(quadratic, label = 'quadratic')
##    pylab.plot(exponential, label = 'exponential')
##    pylab.semilogy()
##    pylab.legend(loc = 'upper left')
##    return
##
##showGrowth(1, 1000)
##pylab.show()

##Iteration Factorial. 
def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

##Recursive Factorial. Fact is called n times. Once again, O(n).
def fact(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return n*fact(n - 1)

##Squares an int. 
##O(n) on the inner loop. O(n) on the start of inner loop. Therefore O(n**2).
def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

##Sum of the digits. O(log n) base 10.
def h(x):
    assert type(x) == int and x >= 0
    answer = 0
    s = str(x)
    for c in s:
        answer += int(c)
    return answer

##Linear search.
def search(L, e):
    for elem in L:
        if elem == e:
            return True
        if elem > e:
            return False
    return False

L = range(100)
print search(L, 0)
print search(L, 50)
print search(L, 100)

##Binary search.
def bSearch(L, e, low, high):
    global numCalls
    numCalls += 1
    if high - low < 2:
        return L[low] == e or L[high] == e
    mid = low + int((high - low)/2)
    if L[mid] == e:
        return True
    if L[mid] > e:
        return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)

def search(L, e):
    return bSearch(L, e, 0, len(L) - 1)

##With a logrithmic algorithm, as the input doubles we only one additional step.
##Slow growth.
L = range(100)
numCalls = 0
search(L, 100)
msg = 'Number of calls when length = '
print msg + str(len(L)) + ' is', numCalls
L = range(200)
numCalls = 0
search(L, 200)
print msg + str(len(L)) + ' is', numCalls
L = range(400)
numCalls = 0
search(L, 400)
print msg + str(len(L)) + ' is', numCalls
L = range(800)
numCalls = 0
search(L, 800)
print msg + str(len(L)) + ' is', numCalls
L = range(1600)
numCalls = 0
search(L, 1600)
print msg + str(len(L)) + ' is', numCalls
L = range(10000000) #ten million
numCalls = 0
search(L, 10000000)
print msg + str(len(L)) + ' is', numCalls

