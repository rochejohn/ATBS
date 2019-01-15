'''
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will
be removed from the beginning and end of the string. Otherwise, the characters specified in the
second argument to the function will be removed from the string.
'''
import re

'''beginning and end ^ $ multiple times'''



def regex_strip(string, strip = 'default'):
    #print(string)
    #print(strip)

    whitespace = re.compile(r'^\s*|\s*$')
    user_def = re.compile(r'strip')

    if strip == 'default':
        sting_stripped = whitespace.sub('',string)
        return sting_stripped

    else:
        return none

print('    hello world    ')
print(len('    hello world    '))

a = regex_strip('    hello world    ')
print(len(a))

b = '          john          '
print(len(b))
c = regex_strip(b)
print(len(c))



