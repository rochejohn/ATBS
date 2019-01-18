'''
Write a program that walks through a folder tree and searches
for exceptionally large files or folders—say, ones that have a file size of more than 100MB.
(Remember, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.
'''

import os


print('This script walks through a folder tree and searches for exceptionally large files or folders.\nOnes that have a file size of more than 100MB.\n\n')


answer = input('Please select the starting point for this script. (Use absolute path only!): ')
bigger_than = int(input('Please select the size in bytes you would like search: '))

if not os.path.exists(answer):
    print('This path does not exist!')

for folder,subfolders,files in os.walk(answer):

    for subfolder in subfolders:
        if subfolder.startswith('.'):
            continue
        subfolder_size = os.path.getsize(subfolder)
        if subfolder_size > 2000:
            print( subfolder + 'is bigger than ' + str(bigger_than) + ' bytes!' )
            print(subfolder +' is ' + subfolder_size + ' bytes!')

    print('\n#####################\n')
    print('FOLDER ' + folder +' ' +str(subfolder_size))
    print()

    for file in files:
        if file.startswith(('.','Deleting')):
            continue
        file_size = os.path.getsize(os.path.join(folder, file))
        if file_size > bigger_than:
            print(file + 'is bigger than ' + str(bigger_than) + ' bytes!')
            print(file + ' is ' + str(file_size) + ' bytes!')


