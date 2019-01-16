'''
Write a program that opens all .txt files in a folder and searches for any line that matches
a user-supplied regular expression. The results should be printed to the screen.
'''


import re,os

print()
print('This program will search all text files in a folder using a specific regulat expression')
print()
print('Simple Regex examples:\nr\'hello world\' or r\'\w\wrld\'')
print()

regex_pattern_user_input = input('Please enter your regex choice without quotes: ')
print()

regex_pattern = re.compile(r'{}'.format(regex_pattern_user_input))



print('Please enter the correct format for your OS for file location using absolute location. (example:/home/docs)')
print()
file_location = input('Please enter a folder where the text files are located: ')
print()
if os.path.isdir(file_location) == True:
    print('Directory Found, changing to directory!')
    print()
    os.chdir(file_location)
    print('Current directory is now {}!'.format(os.getcwd()))
    print()
    print('Will now search for lines within files in this folder containing your provided regex!')

    #text_files_found = txt_regex_pattern.findall\

    for file in os.listdir('.'):
        if file.endswith('.txt'):
            existing_file = open(file)
            each_line = existing_file.readlines()
            for line in each_line:
                match = regex_pattern.search(line)
                if match != None:
                    print()
                    print(line)
                    print()
                    print('The above line(s) matched your regular expression "{}"!'.format(regex_pattern_user_input))



else:
    print('This is not a valid directory')



