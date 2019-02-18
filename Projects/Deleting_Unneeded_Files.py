#! /usr/bin/env python3


'''
Write a program that walks through a folder tree and searches
for exceptionally large files or folders—say, ones that have a file size of more than 100MB.
(Remember, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.
'''

import os


print('\nThis script walks through a folder tree and searches for exceptionally large files.\nOnes that have a file size of more than the selected size.\n\n')


answer = input('Please select the starting point for this script. (Use absolute path only!): ')
bigger_than = int(input('Please select the size in MB you would like search: '))

if not os.path.exists(answer):
    print('This path does not exist!')

for folder,subfolders,files in os.walk(answer):

    for file in files:

        file_size = os.path.getsize(os.path.join(folder,file))
        file_size = round(file_size/1000000,1)
        #print (file_size)

        if file_size >= bigger_than:
            print()
            print(file + ' is ' + str(file_size) + 'MB' + ' Location: ' + os.path.join(folder,file))

