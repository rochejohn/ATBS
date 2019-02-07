'''
Automate the boring stuff chapter 4
Project: Comma Code
Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and a space,
with and inserted before the last item.
'''





def comma_code(lst):

    string1=''

    for item in range(0,len(lst)-1):

        string1 += lst[item].title() + ', '  #added title method for nicer look

    print(string1 + 'and ' + lst[-1].title())


spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

comma_code(spam)