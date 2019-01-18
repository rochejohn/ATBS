'''
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
but no spam002.txt). Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.
'''


import re, shutil, os


#TODO create regex to find files


folder_location = input('Please type the absolute path for the folder which contains the files: ')
if not os.path.exists(folder_location):
    #print('This path does not exist!')
    quit('This Path does not exist, exiting.')

prefix = input('Please type the file prefix: ')

regex = re.compile(r'{}(\d+)'.format(prefix))  # prefix followed by numbers




#TODO create funtion to loop thru files using os.listdir

for file in os.listdir(folder_location):
    if file.startswith(prefix):
        print(file)
