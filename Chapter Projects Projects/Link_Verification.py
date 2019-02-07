'''
Write a program that, given the URL of a web page, will attempt to download every linked page on the page.
The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
'''

'''
When using other pages requests wont load js so only links show from pre js. (very few, except for good example = automate the boring stuff homepage)
'''


'''

Created sample html file to use with broken links
saved raise exception as err to add to output for more detail

script will check for additional file 'Link-Checker-Example.html' before continue.
please ensure file is downloaded.

output:
Two lists, one with working links, second with broken links and explanation of broken link

Added ability to use any site!

'''



import requests,bs4,logging,os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


# Will use downloaded page source and edit some links to broken to produce 404
print('''
Welcome to Link Verification Checker!

You have two options:

1: Use "Link-Checker-Example.html", an example file which contains broken links to display scripts usage!

2: Type in your own full URL, example: "https://automatetheboringstuff.com"

''')

correct_ans = ('1','2')

webpage_file = ''

while True:
    user_answer = input('Please type 1 or 2: ')
    if user_answer in correct_ans:
        break

if user_answer == '1':

    print('\nChecking for file: Link-Checker-Example.html')

    if os.path.exists('Link-Checker-Example.html'):
        print('\nFile Found!')
        webpage_file = open('Link-Checker-Example.html')

    else:
        print('\nFile Not Found!')
        print('\nPlease ensure you have downloaded the file and added to Python working directory!\nExiting!')
        quit()

else:
    url = input('Please enter full URL beginning with HTTP or HTTPS: ')
    if not url.startswith('http'):
        print('Incorrect URL, exiting!')
        exit()
    url_request = requests.get(url)
    webpage_file = url_request.text






####################################################################################
####################################################################################
####################################################################################
############ LINK CHECKER ##########################################################

soup_webpage = bs4.BeautifulSoup(webpage_file,features="html.parser")

soup_webpage_links = soup_webpage.select('a')

found_links = len(soup_webpage_links)

print('Checking for links!\n\n' + str(found_links) + ' Found!')

working_links = []
broken_links = []

for link in range(len(soup_webpage_links)):

    test_link = soup_webpage_links[link].get('href')

    if str(test_link).startswith('http'):
        # deals with absolute links




        try:

            print('Working on new link!')
            test_link_attempt = requests.get(test_link)

            test_link_attempt.raise_for_status()

            working_links.append(test_link)

        except Exception as err:
            broken_links.append(test_link + ' is broken with the following error raised: ' + str(err))

    else:
        # deals with relative links

        if test_link == None:
            continue


        test_link = url + test_link

        #test_link_attempt = requests.get(test_link)

        try:
            print('Working on new link!')

            test_link_attempt = requests.get(test_link)
            test_link_attempt.raise_for_status()
            working_links.append(test_link)

        except Exception as err:
            broken_links.append(test_link + ' link raised: ' + str(err))









##### PRINTING SECTION  ###################################
##### PRINTING SECTION  ###################################
##### PRINTING SECTION  ###################################


print('\nAll links have now been tested!')
print()
print()

print(str(len(working_links)) + ' are Working Links:')
print()
for link in range(len(working_links)):
    print(working_links[link])

print()
print()
print(str(len(broken_links)) + ' are broken Links:')
print()
for link in range(len(broken_links)):
    print(broken_links[link])

print()
print('####################################################################################################')
print('####################################################################################################')
print()
print(str(len(working_links)) + ' links are loading successfully, and ' + str(len(broken_links)) + ' links have issues!')

print()
print("Script Finished, please review links above!")

    

