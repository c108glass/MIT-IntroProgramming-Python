##Lecture 6
##Recursion
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Divide and conquer. Small problems are eaiser to solve.
##Solutions of small problems can be easily combined to find solutions of big problems.
##Recurison is a way of describing problems and designing solutions. Find a base case, find the recursive case.

##The classic Tower of Hanoi puzzle.
##n = number of disks in stack, f = from stack, t = target stack, s = spare stack.
def Hanoi(n, f, t, s):    
    if n == 1:
        print 'move from ' + f + ' to ' + t
    else:
        Hanoi(n-1, f, s, t)
        Hanoi(1, f, t, s)
        Hanoi(n-1, s, t, f)

print 'Solution for stack of 1 is:'
Hanoi(1, 'f', 't', 's')
print 'Solution for stack of 2 is:'
Hanoi(2, 'f', 't', 's')
print 'Solution for stack of 3 is:'
Hanoi(3, 'f', 't', 's')

##Find a palindrome.
##Converts string to lowercase and forms the word.
def toChars(s):
    import string
    s = string.lower(s) 
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c 
    return ans

##Then isPal() takes a word and compares the first and last characters, working its way to the middle.
##Word will contain an even or odd number of characters so we need <=1 to determine when we are done with the word.
##If <=1, then its true/its finished with the word.
##Else, if first and last character are the same, then it moves on to the next set by
##taking what's left over and plugging it back into the function to repeat the process. isPal(s[1:-1])
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

print isPalindrome('Guttag')
print isPalindrome('Guttug')
print isPalindrome('Able was I ere I saw Elba')
print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')

##This breaks down the process of examining the word and prints each step.
def isPalPrint(s, indent = '  '):
    print indent, 'isPalPrint called with', repr(s)
    if len(s) <= 1:
        print indent, 'About to return True from base case'
        return True
    else:
        ans = s[0] == s[-1] and isPalPrint(s[1:-1], indent + indent)
        print indent, 'About to return', ans, 'for', s
        return ans

def isPalindromePrint(s):
    """Return True if s is a palindrome and False otherwise"""
    return isPalPrint(toChars(s))

print 'Test Guttag \n', isPalindromePrint('Guttag')
print 'Test Guttug \n', isPalindromePrint('Guttug')

##Fibonacci and the rate of breeding rabbits.
##Model: Start with newborn pair of rabbits. One male and one female.
##Assume they can start breeding at one month and they have a gestation period of one month.
##Assume they never die and each female produces another pair(one male, one female).
##How many female rabbits will there be at the end a year?
def fib(x):
    """assumes x an int >= 0
        Returns. Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1: ##At months 0: 1 newborn female. At month 1: 1 adult pregnant female. Either case = 1 female. 
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        print ('fib of', i, '=', fib(i))

print 'Test 1 month: \n', testFib(1)
print 'Test 5 months: \n', testFib(5)
print 'Test 8 months: \n', testFib(8)
