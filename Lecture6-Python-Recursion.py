##Lecture 6
##Recursion
##Intro to Computer Science And Programming - MIT
##https://ocw.mit.edu

##Divide and conquer. Small problems are eaiser to solve.
##Solutions of small problems can be easily combined to find solutions of big problems.
##Recurison is a way of describing problems and designing solutions. 

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

##This takes a word and compares the first and last characters, working its way to the middle of the word.
##Word will contain an even or odd number of characters so we need <=1 to determine when we are done with the word.
##If <=1, then its true/its finished with the word.
##Else, if first and last character are the same, then it moves on to the next set by
##taking what's left over and plugging it back into the function to repeat the process.
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
