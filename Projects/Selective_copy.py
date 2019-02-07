'''
Write a program that walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.
'''


file_loc = input('\nPlease input the directory location you would like to search: ')

import os,shutil,datetime




try:
    os.mkdir('PDF_TXT_copied')

except:
    print('Destination folder already exists!')

print('Now copying all PDF and TXT files from folders and sub-folders!')


for folders,subfolders,files in os.walk(file_loc):


    for file in files:
        if file.endswith(('.pdf','.txt')):
            print(os.path.join(folders,file))
            print(file)
            shutil.copy(os.path.join(folders,file),'PDF_TXT_copied')

print('Done, you can now find a copy of your files under PDF_TXT_copied folder!!')






