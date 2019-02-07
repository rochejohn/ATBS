'''
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt
but no spam002.txt). Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.
'''


import re, shutil, os,sys


#TODO create regex to find files


folder_location = input('Please type the absolute path for the folder which contains the files: ')
#folder_location = '/users/john/testfiles'


if not os.path.exists(folder_location):
    sys.exit('This Path does not exist, exiting.')

prefix = input('Please type the file prefix: ')
#prefix = 'spam'


regex = re.compile(r'({})(\d+)(\.\w+)$'.format(prefix))  # prefix followed by numbers

file_names = []

for file in os.listdir(folder_location):

    if file.startswith(prefix):
        file_names.append(file)


sorted_file_names = sorted(file_names)
#print(sorted_file_names)


match = regex.search(sorted_file_names[0])
#print(match.group(0))

zero_padding = len(match.group(2))

file_ext = match.group(3)
#print(file_ext)

#print(sorted_file_names)

#print(zero_padding)

gap = None

for file_index in range(len(sorted_file_names)-1):



    current_file = sorted_file_names[file_index]
    next_file = sorted_file_names[file_index+1]

    match_current = regex.search(current_file)
    match_current = match_current.group(2).lstrip('0')
    #print(match_current)

    #print('to')

    match_next = regex.search(next_file)
    match_next = match_next.group(2).lstrip('0')
    #print(match_next)
    #print()

    if int(match_current)+1 != int(match_next):
        print('\nA gap has been found in the file numbering!\n')
        gap = 'found'

        break

file_new_num = 1

if gap != None:

    print('\nAs files are in a sorted order and a gap has been found, will now fix numbering!\n')

    for file in sorted_file_names:
        shutil.move(os.path.join(folder_location,file),os.path.join(folder_location,prefix+str(file_new_num).zfill(zero_padding)+file_ext))

        print('File renaming: ' + prefix+str(file_new_num).zfill(zero_padding)+file_ext)

        file_new_num += 1

else:
    print("\nNo gap has been found.")
