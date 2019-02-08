# Automate The Boring Stuff Projects

## Table of Contents


- [Introduction](#Introduction)
- [Scripts](#Scripts)
- [Book Reference](#Reference)
- [Required Modules](#Required-Modules)


## Introduction

> Template In Progress

> At the end of each chapter of the "Automate The Boring Stuff" book are multiple projects with no available solutions, which encourages students to create their own code.

> Below are my Python Script solution's for each of hte Chapter Project's.

> Also added a GIF/Screenshots for each script to show usage.

> For reference to the book used and also each required third party module required please see the 1) "Book Reference and "Required Modules" sections.
---
## Scripts

### Chapter 3 – Functions

- [Collatz Sequence & Input Validation](#Collatz-sequence--input-validation)

### Chapter 4 – Lists

- [Comma Code](#Comma-Code)
- [Character Picture Grid](#Character-Picture-Grid)

### Chapter 5 – Dictionaries and Structuring Data

- [Fantasy Game Inventory / List to Dict Function](#Fantasy-Game-Inventory)

### Chapter 6 – Manipulating Strings

- [Table Printer](#Table-Printer)

### Chapter 7 – Pattern Matching with Regular Expressions

- [Strong Password Detection](#Strong-Password-Detection)
- [Regex Version of strip()](#regex-version-of-strip)

### Chapter 8 – Reading and Writing Files

- [Extending the Multiclipboard](#Extending-the-Multiclipboard)
- [Mad Libs](#Mad-Libs)
- [Regex Search](#Regex-Search)

### Chapter 9 – Organizing Files

- [Selective Copy](#Selective-Copy)
- [Deleting Unneeded Files](#Deleting-Unneeded-Files)
- [Filling in the Gaps](#Filling-in-the-Gaps)

### Chapter 10 – Debugging

- [Debugging Coin Toss](#Debugging-Coin-Toss)

### Chapter 11 – Web Scraping

- [Command Line Emailer](#Command-Line-Emailer)
- [Image Site Downloader](#CImage-Site-Downloader)
- [2048](#2048)
- [Link Verification](#Link-Verification)


### Chapter 12 – Working with Excel Spreadsheets

- [Multiplication Table Maker](#Multiplication-Table-Maker)
- [Blank Row Inserter](#Blank-Row-Inserter)
- [Spreadsheet Cell Inverter](#Spreadsheet-Cell-Inverter)
- [Text Files to Spreadsheet](#Text-Files-to-Spreadsheet)
- [Spreadsheet to Text Files](#Spreadsheet-to-Text-Files)



### Chapter 14 – Working with CSV Files and JSON Data

- [Excel-to-CSV Converter](#Excel-to-CSV-Converter)

### Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

- [Required Modules](#Required-Modules)

### Chapter 16 – Sending Email and Text Messages

- [Umbrella Reminder](#Umbrella-Reminder)
- [Auto Unsubscriber](#Auto-Unsubscriber)


---

# **Scripts & GIFs**

---

## Chapter 3 Functions

### Collatz Sequence & Input Validation

* [The Collatz Sequence & Input Validation - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/collatz.py)

#### Details
---
> Part 1: The Collatz Sequence.
>> Natural numbers when run through a specific function based on being odd or even, specifically stating that regardless of the initial number the series will eventually reach the number 1.

> Part 2: Check User Input for a valid number.
---

#### The Collatz Sequence & Input Validation GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c3/collatz:validation.gif)


---

## Chapter 4 Lists

### Comma Code

* [Comma Code - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Comma_Code.py)

#### Details
---
> Comma Code Overview:
- This Function takes a list value as an argument and returns a string with all the items separated by a comma and a space, with "and" inserted before the last item.
---

#### Comma Code GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c4/Comma_code.gif)

---

### Character Picture Grid

* [Character Picture Grid - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Character_Picture_Grid.py)

#### Details
---
>  Character Picture Grid overview:
- Using nested for loops to flip an image 90 degrees.
- Using time.sleep to slow print to give illusion of drawing
---

#### Character Picture Grid GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c4/Character_Picture_Grid.gif)

---

## Chapter 5 Dictionaries and Structuring Data

### Fantasy Game Inventory

* [Fantasy Game Inventory - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Fantasy_Game_Inventory.py)

#### Details
---
> Part 1:
- Create a data structure to model the player’s inventory, a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has, and function to display items.

> Part 2:
- Create a funtion to add items in a list to the disctionary.
---

#### Fantasy Game Inventory GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c5/Fantasy_Game:List:Dict.gif)

---

## Chapter 6 Manipulating Strings

### Table Printer

* [Table Printer - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Table_Printer.py)

#### Details
---
> Table Printer Overview:
- A function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
---

#### Table Printer GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c6/Table_Printer.gif)


---
## Chapter 7 Pattern Matching with Regular Expressions

### Strong Password Detection

* [Strong Password Detection - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Strong_password_Detection.py)

#### Details
---
> Strong Password Detection Overview:
- A function which uses regular expressions to make sure the password string it is passed is strong.
- Defines requirements for password.
- Checks if at least eight characters long
- Contains both uppercase and lowercase characters
- And at least one digit. 
---

#### Strong Password Detection GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c7/Strong_Password.gif)

---

### Regex Version of strip()

* [Regex Version of strip() - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Regex_strip.py)

#### Details
---
>  Regex Version of strip() overview:
-  A function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.
- Contains two examples with the length of each string to easy display difference.
---

#### Regex Version of strip() GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c7/Regex_strip.gif)


---

## Chapter 8 Reading and Writing Files

### Extending the Multiclipboard

* [Extending the Multiclipboard - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Extending_the_Multiclipboard.py)

#### Details
---
> MultiClipBoard Overview:
- Command line ClipBoard with the following usage:
- Extending_the_Multiclipboard.py {save} <keyword> - Saves clipboard to to keyword.
- Extending_the_Multiclipboard.py <keyword> - Loads keyword to clipboard.
- Extending_the_Multiclipboard.py {list} - Lists all keywords to available in clipboard.
- Extending_the_Multiclipboard.py {delete} <keyword> - Removes keyword data.
- Extending_the_Multiclipboard.py {delete} - Removes all data.

---

#### Extending the Multiclipboard GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c8/Multi_ClipBoard.gif)

---

### Mad Libs

* [Mad Libs - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Mad_Libs.py)

#### Details
---
> Mad Libs overview:
-  A Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
- Also included a HardCoded example for user to test with.
---

#### Mad Libs GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c8/Mad_Libs.gif)

---

### Regex Search

* [Regex Search - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Regex_Search.py)

#### Details
---
> Regex Search overview:
-  Opens all ".txt" files in a specific folder and searches for any line that matches
a user-supplied regular expression.
- Each line is then printed to the screen and also states which file the line came from.

#### Regex Search GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c8/Regex_Search.gif)

---

## Chapter 9 Organizing Files

### Selective Copy

* [Selective Copy - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Selective_copy.py)

#### Details
---
> Selective Copy Overview:
- Asks users for location.
- Script walks through a folder tree (folders & sub-folders and searches for specific files (.pdf or .jpg).
- Copy files from whatever location they are in to a newly created folder.

---

#### Selective Copy GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c9/Selective_Copy.gif)

---

### Deleting Unneeded Files

* [Deleting Unneeded Files - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Deleting_Unneeded_Files.py)

#### Details
---
> Deleting Unneeded Files overview:
- Asks users for specific directory and file size.  
- This script walks through the folder tree and searches for files a file size of more than the user selected size.
- Outputs all files and absolute location that are bigger than specified size to screen.
---

#### Deleting Unneeded Files GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c9/Delete_Large_Files.gif)

---

### Filling in the Gaps

* [Filling in the Gaps - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Filling_in_the_Gaps.py)

#### Details
---
> Filling in the Gaps overview:
-Uses Regex object groups to seperate: File name, file number, and file extension.
-  Finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Rename's all the later files to close this gap.


#### Filling in the Gaps GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c9/Filling_gaps.gif)

---

## Chapter 10 Debugging

### Debugging Coin Toss

* [Debugging Coin Toss - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Debugging_Coin_Toss.py)

#### Details
---
> Debugging Coin Toss Overview:
- Book provided script which you have to insert debugging statements to find the bugs.
- Multiple Bugs, main bug is user is asked for "Heads" of "Tails", however original script only checks for "1" or "2", so user is always incorrect.

---

#### Debugging Coin Toss GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c10/Debugging_coin.gif)

---

## Chapter 11 Web Scraping

### Command Line Emailer

* [Command Line Emailer - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/command_line_emailer.py)

#### Details
---
> Command Line Emailer Overview:
- This script uses throw away email and password already changed!
- Script takes an email address and string of text and then, using Selenium webdriver, logs into your configured email account and sends an email of the string to the provided address.
- Usage: Two Methods
1: command_line_emailer.py {recipient email address} {The text to send in the email}
2: Supply no arguments, this will open up the prompts!

---

#### Command Line Emailer GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c11/command_email.gif)

---

### Image Site Downloader

* [Image Site Downloader - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Image_Site_Downloader.py)

#### Details
---
> Image Site Downloader overview:
- Script uses Imgur site
- Allow user to search for own category
- Creates folder imgur-downloads
- Creates sub-folder with search name to download up to 10 images only (set limit)
- Displays any network errors, and continues on, with Try/Except.
---

#### Image Site Downloader GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c11/Image_Site_Downloader.gif)

---

### 2048

* [2048 - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/2048.py)

#### Details
---
> 2048 overview:
- Uses Selenium to open game at: https://gabrielecirulli.github.io/2048/ 
- Keep sending up, right, down, and left keystrokes to automatically play the game until it is over.
- Pulls down Final score and prints to screen.
- Closes browser.


#### 2048 GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c11/2048_automated.gif)

---

### Link Verification

* [Link Verification - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Link_Verification.py)

#### Details
---
> Link Verification overview:
-Uses Requests module and Beautiful Soup.
- Given the URL of a web page, will attempt to download every linked page on the page. Creates two lists, 1) Working Links, 2) Broken Links.
- Broken Links are saved with the description of the error thrown.
-Two Options:
1) Use pre-made HTML page in Github with examples of broken and working links.
2) User enters own URL. (Requests module wont load JS so URL example is "https://automatetheboringstuff.com"


#### Link Verification Option 1 GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c11/Link_verification_1.gif)


#### Link Verification Option 2 GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c11/Link_verification_2.gif)

---

## Chapter 12 Working with Excel Spreadsheets

### Multiplication Table Maker

* [Multiplication Table Maker - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Multiplication_Table_Maker.py)

#### Details
---
> Multiplication Table Maker Overview:
- Uses Openpyxl module to work with Spreadsheets
- Script takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet.
- Usage: multiplicationTable.py 6
- Row 1 and column A are in "Bold" and are "Frozen" in place to read sum easier.

---

#### Multiplication Table Maker GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Multi_table.gif)

---
#### Multiplication Spreadsheet from Script Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Multi-table-output.png" width="300" height="300" />
---


### Blank Row Inserter

* [Blank Row Inserter - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Blank_Row_Inserter.py)

#### Details
---
> Blank Row Inserter overview:
- Uses Openpyxl module to work with Spreadsheets
- Script takes two integers and a filename string as command line arguments.
- Let’s call the first integer N and the second integer M.
- Starting at row N, the program should insert M blank rows into the spreadsheet.
- For example: BlankRowInserter.py 3 2 myExample.xlsx
- Saves new Spreadsheet as "modified_with_blank_inserts.xlsx"
---

#### Blank Row Inserter GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Blank_row_Inserter.gif)

---

#### Blank Row Inserter Script Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Blank_row.png" width="300" height="300" />


---

### Spreadsheet Cell Inverter

* [Spreadsheet Cell Inverter - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Spreadsheet_Cell_Inverter.py)

#### Details
---
> Spreadsheet Cell Inverter overview:
- Uses Openpyxl module to work with Spreadsheets
- Script invert's the row and column of the cells in the spreadsheet.
- For example, the value at row 5, column 3 will be at row 3, column 5 (and vice versa).


#### Spreadsheet Cell Inverter GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Spreadsheet_Inverter.gif)

---

#### Spreadsheet Cell Inverter: Before Inverted
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Before_Inverted.png" width="300" height="300" />


---


#### Spreadsheet Cell Inverter: After Inverted
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/After_Inverted.png" width="300" height="300" />


---


### Text Files to Spreadsheet

* [Text Files to Spreadsheet - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Text_Files_to_Spreadsheet.py)

#### Details
---
> Text Files to Spreadsheet overview:
- Reads in the contents of several text files.
- Inserts those contents into a spreadsheet, with one line of text per row.
- The lines of the first text file will be in the cells of column A
- The lines of the second text file will be in the cells of column B, and so on.
- For the first file, output the first line to column 1, row 1.
- The second line should be written to column 1, row 2, and so on.


#### Text Files to Spreadsheet GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/text_to_spreadsheet.gif)

---

#### Text Files to Spreadsheet: Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Spreadsheet_to_texts::text_to_Spread.png" width="300" height="300" />


---

### Spreadsheet to Text Files

* [Spreadsheet to Text Files - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Spreadsheet_to_Text_Files.py)

#### Details
---
> Spreadsheet to Text Files overview:
- Open's a spreadsheet and write's the cells of column A into one text file, and the cells of column B into another text file, and so on.


#### Spreadsheet to Text Files GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/spreadsheet_to_text.gif)

---

#### Spreadsheet to Text Files: Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c12/Spreadsheet_to_text_Output.png" width="300" height="300" />


---

## Chapter 14 Working with CSV Files and JSON Data

### Excel-to-CSV Converter

* [Excel-to-CSV Converter - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Excel-to-CSV_Converter.py)

#### Details
---
> Excel-to-CSV Converter Overview:
- Goes through every Excel File in Directory
- Then goes through every worksheet in each Excel Sheet
- Creates a CSV File for every single Worksheet and outputs to same directory.
- CSV name structure is Excel Filename and worksheet name joined.


---

#### Excel-to-CSV Converter GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c14/Excel-to-CSV%20Converter.gif)


---

#### Excel Before:
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c14/Excel-to-CSV%20Converter-EXCEL.png" width="300" height="300" />

---

#### CSV After:
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c14/Excel-to-CSV%20Converter-CSV.png" width="300" height="300" />

---

## Chapter 15 Keeping Time, Scheduling Tasks, and Launching Programs

### Prettified Stopwatch

* [Prettified Stopwatch - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Prettified_Stopwatch.py)

#### Details
---
> Prettified Stopwatch Overview:
- Creates a Stop Watch with Justified Text to make it display better.
- Excepts KeyBoard Interrupt as way to close.
-Copies Lap times to Clipboard when finished.

---

#### Prettified Stopwatch GIF
---

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c15/Pretty_StopWatch.gif)


---

## Chapter 16 Sending Email and Text Messages

### Umbrella Reminder

* [Umbrella Reminder - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Umbrella.py)

#### Details
---
> Umbrella Script Overview:
- Takes arguement from command line for location. (Umbrella.py {location})
- Calls and Authenticate to "OpenWeatherMap API" and pulls down json for location.
- Converts JSON to Dictionary, pulls Weather data.
- Appends Specific Weather Data to String variable.
- Condition to check to add "Need Umbrella" string, adds string if True.
- Finished String variable used as arguement to Twilio module
- Authenicate with Twilio to send string variable as SMS.
- SMS received on phone.
---

#### Umbrella Reminder GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c17/umbrella.gif)

---
#### Text Received from Script Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c17/weather_text.jpg" width="300" height="500" />

---

### Auto Unsubscriber

* [Auto Unsubscriber - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Auto_Unsubscriber.py)

#### Details
---
> Unsubscribe Email overview:
- Gmail Users only
- Requests Users Email and Password 
- Uses module IMAPCLIENT to fetch specific email
- Uses module PYZMAIL to extract HTML from IMAPCLIENT objects
- Uses Beautiful Soup to extract Tags with Unsubsribe links
- Uses WebBrowser module to open each unsubscribe link in Browser
- Script also displays how many emails it checks, how many unsubscribe links are found and also email senders.

---

#### Auto Unsubscriber GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c17/EMAIL_UNSUB.gif)


---


## Reference

> Automate The Boring Stuff is a free book written by Al Sweigart for learning Python 3. 
> 
> This book is available at the following website: https://automatetheboringstuff.com




---
## Required Modules

### You can install all of the modules required for the above scripts by running the commands listed next.

- **pip install send2trash**

- **pip install requests**

- **pip install beautifulsoup4**

- **pip install selenium**

- **pip install openpyxl==2.1.4**

- **pip install PyPDF2**

- **pip install python-docx (install python-docx, not docx)**

- **pip install imapclient**

- **pip install pyzmail**

- **pip install twilio**




