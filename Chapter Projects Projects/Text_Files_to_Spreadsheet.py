'''
Write a program to read in the contents of several text files (you can make the text files yourself)
and insert those contents into a spreadsheet, with one line of text per row. The lines of the first
text file will be in the cells of column A, the lines of the second text file will be
in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, one string per line in the file.
For the first file, output the first line to column 1, row 1. The second line should be written to
column 1, row 2, and so on. The next file that is read with readlines() will be written to column 2,
the next file to column 3, and so on.
'''

import openpyxl

file1 = open('/users/john/testfiles/A1.txt','r')
file1_lines = file1.readlines()
file1.close()

file2 = open('/users/john/testfiles/B1.txt','r')
file2_lines = file2.readlines()
file2.close()


file3 = open('/users/john/testfiles/C1.txt','r')
file3_lines = file3.readlines()
file3.close()


file4 = open('/users/john/testfiles/D1.txt','r')
file4_lines = file4.readlines()
file4.close()


wb = openpyxl.Workbook()
sheet = wb.active

all_files_list= [file1_lines,file2_lines,file3_lines,file4_lines]


col = 0
start_row = 0

for file in all_files_list:
    col+=1
    start_row+=1
    row=start_row
    for line in file:
        sheet.cell(row=row,column=col).value = line
        row += 1

wb.save('Text_files_to_spreadsheet.xlsx')

print('\nFiles have been successfully loaded into the spreadsheet named "Text_files_to_spreadsheet.xlsx"')


