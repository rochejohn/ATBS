'''

Excel can save a spreadsheet to a CSV file with a few mouse clicks,
but if you had to convert hundreds of Excel files to CSVs, it would take hours of clicking.
Using the openpyxl module from Chapter 12, write a program that reads all the Excel files
in the current working directory and outputs them as CSV files.

A single Excel file might contain multiple sheets;
you’ll have to create one CSV file per sheet.
The filenames of the CSV files should be <excel filename>_<sheet title>.csv,
where <excel filename> is the filename of the Excel file without the file extension
(for example, 'spam_data', not 'spam_data.xlsx') and <sheet title> is the string
from the Worksheet object’s title variable.

This program will involve many nested for loops. The skeleton of the program will look something like this:

 for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                # Append each cell's data to rowData.

            # Write the rowData list to the CSV file.

        csvFile.close()

Download the ZIP file excelSpreadsheets.zip from http://nostarch.com/automatestuff/,
and unzip the spreadsheets into the same directory as your program.
You can use these as the files to test the program on.

'''


import os, openpyxl,csv

excelspreadsheets = input('Please input absolute location for excel spreadsheets: ')

os.chdir(excelspreadsheets)

for excelFile in os.listdir('.'):



    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue

    print('\nFound Excel File ' + excelFile)

    wb = openpyxl.load_workbook(excelFile)
    # Loop through every sheet in the workbook.
    for sheetName in wb.sheetnames:

        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]

        # Create the CSV filename from the Excel filename and sheet title.
        csv_filename = excelFile[:len(excelFile)-5] +'_'+sheetName

        csv_file = open(csv_filename+'.csv', 'w', newline='') #newline specific to windows

        #print(csv_filename)

        # Create the csv.writer object for this CSV file.


        # Loop through every row in the sheet.

        for rowNum in range(1, sheet.max_row+1):


            rowData = []    # append each cell to this list

            row = sheet[rowNum]

            # Loop through each cell in the row.

            for cellobj in row:

            # Append each cell's data to rowData.
                rowData.append(cellobj.value)

            # Write the rowData list to the CSV file.
            write_csv = csv.writer(csv_file)


            write_csv.writerow(rowData)

            #print(rowData)



        csv_file.close()

        print('\nCreated CSV file: ' + csv_filename)



print('All Excel files have now been converted and are stored in the same directory as Excel.')

























