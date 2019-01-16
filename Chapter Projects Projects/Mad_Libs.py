'''
Finished notes:
Added default built in string if user wants to test without a file.
Also added os.getcwd() to show where file is saved to!
'''



'''
Create a Mad Libs program that reads in text files and
lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
'''

'''
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The results should be printed to the screen and saved to a new text file.
'''

import re,os

finder = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

print()
print('''Create a Mad Libs program that reads in text files and
lets the user add their own text anywhere the word
ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.''')

print('\nPlease leave blank to use the hardcoded example!')

user_select_file = input('\nWelcome!\n\nPlease enter the name of the file you would like to edit: ')

#hardcoded example for user with no example available

panda = '''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.'''

if user_select_file == '':
    file_contents = panda
else:
    user_file = open(user_select_file)
    file_contents = user_file.read()
    user_file.close()

match = finder.findall(file_contents)
print()
print(file_contents)
print()


for word_type in match:
    ans = input('Please enter a {}: '.format(word_type))
    file_contents= file_contents.replace(word_type,ans)

print()
print(file_contents)


'''Open file and added the changed contents, added the location of the file also for easy to find'''

print('\nThe output is now saved to the text file "Mad_Libs_Output in the directory "{}"'.format(os.getcwd()))

fin_file = open('Mad_Libs_Output.txt','w')

fin_file.write(file_contents)

fin_file.close()






