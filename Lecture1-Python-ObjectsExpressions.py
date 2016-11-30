Python 2.5.4 (r254:67916, Dec 23 2008, 15:10:54) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.4      
>>> 3
3
>>> type(3)
<type 'int'>
>>> 3.2
3.2000000000000002
>>> type(3.2)
<type 'float'>
>>> type(True)
<type 'bool'>
>>> True and False
False
>>> None
>>> type(None)
<type 'NoneType'>
>>> 'a'
'a'
>>> type('a')
<type 'str'>
>>> 'ab'
'ab'
>>> "ab"
'ab'
>>> type('123')
<type 'str'>
>>> type(123)
<type 'int'>
>>> 3+2
5
>>> 3/2
1
>>> 3.0/2.0
1.5
>>> 'a' + 'b'
'ab'
>>> 3 3
SyntaxError: invalid syntax
>>> 'a' + 3

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    'a' + 3
TypeError: cannot concatenate 'str' and 'int' objects
>>> 'a' + '3'
'a3'
>>> 'a' + str(3)
'a3'
>>> int('3')
3
>>> int('.0')

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int('.0')
ValueError: invalid literal for int() with base 10: '.0'
>>> int(2.1)
2
>>> 
