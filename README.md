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

- [Required Modules](#Required-Modules)

### Chapter 9 – Organizing Files

- [Required Modules](#Required-Modules)

### Chapter 10 – Debugging

- [Required Modules](#Required-Modules)

### Chapter 11 – Web Scraping

- [Required Modules](#Required-Modules)

### Chapter 12 – Working with Excel Spreadsheets

- [Required Modules](#Required-Modules)

### Chapter 14 – Working with CSV Files and JSON Data

- [Required Modules](#Required-Modules)

### Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

- [Required Modules](#Required-Modules)

### Chapter 16 – Sending Email and Text Messages

- [Umbrella Reminder](#Umbrella-Reminder)
- [Auto Unsubscriber](#Auto-Unsubscriber)


---

### **Scripts & GIFs**

---

## Chapter 3 – Functions
### Collatz Sequence & Input Validation

* [The Collatz Sequence & Input Validation - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/collatz.py)

### Details
---
> Part 1: The Collatz Sequence.
>> Natural numbers when run through a specific function based on being odd or even, specifically stating that regardless of the initial number the series will eventually reach the number 1.

> Part 2: Check User Input for a valid number.
---

### The Collatz Sequence & Input Validation GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c3/collatz:validation.gif)


---

## Chapter 4 Lists
### Comma Code

* [Comma Code - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Comma_Code.py)

### Details
---
> Comma Code Overview:
- This Function takes a list value as an argument and returns a string with all the items separated by a comma and a space, with "and" inserted before the last item.
---

### Comma Code GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c4/Comma_code.gif)

---

### Character Picture Grid

* [Character Picture Grid - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Character_Picture_Grid.py)

### Details
---
>  Character Picture Grid overview:
- Using nested for loops to flip an image 90 degrees.
- Using time.sleep to slow print to give illusion of drawing
---

### Character Picture Grid GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c4/Character_Picture_Grid.gif)

---

## Chapter 5 Dictionaries and Structuring Data
### Fantasy Game Inventory

* [Fantasy Game Inventory - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Fantasy_Game_Inventory.py)

### Details
---
> Part 1:
- Create a data structure to model the player’s inventory, a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has, and function to display items.

> Part 2:
- Create a funtion to add items in a list to the disctionary.
---

### Fantasy Game Inventory GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c5/Fantasy_Game:List:Dict.gif)

---

## Chapter 6 Manipulating Strings
### Table Printer

* [Table Printer - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Table_Printer.py)

### Details
---
> Table Printer Overview:
- A function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
---

### Table Printer GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c6/Table_Printer.gif)



---











## Chapter 7 Pattern Matching with Regular Expressions
### Strong Password Detection

* [Strong Password Detection - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Strong_password_Detection.py)

### Details
---
> Comma Code Overview:
- This Function takes a list value as an argument and returns a string with all the items separated by a comma and a space, with "and" inserted before the last item.
---

### Strong Password Detection GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c7/Strong_Password.gif)

---

### Regex Version of strip()

* [Regex Version of strip() - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Regex_strip.py)

### Details
---
>  Character Picture Grid overview:
- Using nested for loops to flip an image 90 degrees.
- Using time.sleep to slow print to give illusion of drawing
---

### Regex Version of strip() GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c7/Regex_strip.gif)

---





















































































## Chapter 16 Sending Email and Text Messages
### Umbrella Reminder

* [Umbrella Reminder - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Umbrella.py)

### Details
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

### Umbrella Reminder GIF

![GIF](https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c17/umbrella.gif)

---
### Text Received from Script Output
<img src="https://github.com/rochejohn/ATBS/blob/master/Projects/gifs/c17/weather_text.jpg" width="300" height="500" />

---

### Auto Unsubscriber

* [Auto Unsubscriber - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Auto_Unsubscriber.py)

### Details
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

### Auto Unsubscriber GIF

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




