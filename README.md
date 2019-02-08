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

- [Collatz Sequence & Input Validation](#Collatz-Sequence-&-Input-Validation)

### Chapter 4 – Lists

- [Required Modules](#Required-Modules)

### Chapter 5 – Dictionaries and Structuring Data

- [Required Modules](#Required-Modules)

### Chapter 6 – Manipulating Strings

- [Required Modules](#Required-Modules)

### Chapter 7 – Pattern Matching with Regular Expressions

- [Required Modules](#Required-Modules)

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

## Chapter 16 Sending Email and Text Messages
### Umbrella Reminder

* [Umbrella Reminder - Code](https://github.com/rochejohn/ATBS/blob/master/Projects/Umbrella.py)

### Details
---
> Umbrella Script Steps:
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




