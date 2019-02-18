#! /usr/bin/env python3


'''
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will
be removed from the beginning and end of the string. Otherwise, the characters specified in the
second argument to the function will be removed from the string.
'''
import re,time

'''beginning and end ^ $ multiple times'''



def regex_strip(string, strip = ''):

    whitespace = re.compile(r'^\s*|\s*$')
    user_def = re.compile(r'^({s})*|({s})*$'.format(s=strip))

    if strip == '':
        string_stripped = whitespace.sub('',string)
        return string_stripped

    else:
        string_stripped = user_def.sub('',string)
        return string_stripped

####################################################################################################
####################################################################################################

# Example one, take argument 'a' and remove from string

string_a = 'aaaajohnaaaa'
#12 Char long // will remove all 'a'
print()
print('Example 1',end=' ')
print(string_a)
#print out example

print('The length =', end=' ')
print(len(string_a))
# prints length of 12 before remove with strip

string_a = (regex_strip(string_a,'a'))
#funtion called
print()
print('Example 1 stripped:',end=' ')
print(string_a)
#print out after strip

print('The length =', end=' ')
print(len(string_a))
# function takes in 'string a' and the parameter 'a' to use for strip // returns john with
# all 'a' removed from beginning and end of string

print()
print('####################################################################################################')
print()
####################################################################################################
####################################################################################################

# Example two, no argument given, defaults to remove whitespace

string_whitespace = '          john    '

print('Example 2',end=' ')
print(string_whitespace)
#print out example

print('The length =', end=' ')
print(len(string_whitespace))
# prints length of example before remove with strip

string_whitespace = regex_strip(string_whitespace)
#note no argument given for second placeholder
#funtion called!
print()
print('Example 2',end=' ')
print(string_whitespace)
#print out after strip

print('The length =', end=' ')
print(len(string_whitespace))
# function takes in 'string a' and the parameter 'a' to use for strip // returns john with
# all 'a' removed from beginning and end of string

print()
print('####################################################################################################')
print()

while True:

    ans = input('Would you like to test with an example? y/n: ')

    if ans.lower() == 'y':
        supplied_string = input('Please type your string: ')
        supplied_strip = input('Please supply the parameter to strip. (Leave blank for whitespace): ')
        len_supplied_string = len(supplied_string)
        print('Your input string is "%s" with a length of "%s"' %(supplied_string,len_supplied_string))

        print('Applying strip function as per your supplied parameters...')
        time.sleep(2)

        stripped_string = regex_strip(supplied_string,supplied_strip)
        len_stripped_string = len(stripped_string)
        print('Your stripped string is "%s" with a length of "%s"' %(stripped_string,len_stripped_string))
        continue



    elif ans == 'n':
        print('Goodbye for now!')
        break

    else:
        print('Invalid option! Please enter y/n....')







