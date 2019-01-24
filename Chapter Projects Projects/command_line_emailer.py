'''
Write a program that takes an email address and string of text on the command line and then,
using Selenium, logs into your email account and sends an email of the string to the provided address.
(You might want to set up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook or Twitter account.
'''

'''
This script uses throw away email!
Usage: Two Methods

1: command_line_emailer.py {recipient email address} {The text to send in the email}

2: Supply no arguments, this will open up the prompts!

'''


# This will use command line arguments
# Gmail ONLY
# example will be (python command_line_emailer.py email-address email-body)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging,time,sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)



url = 'https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/'

email = 'johnroche.ATBS@gmail.com'
password = 'abbc1234!'

if len(sys.argv) > 1:
    email_recipient = sys.argv[1]
    logging.debug(email_recipient)
    body = ' '.join(sys.argv[2:])
    logging.debug(body)


else:
    print('\nHello!\n\nWelcome to the command line version!\n')
    email_recipient = input('Who would you like to send the email to: ')
    body = input('What would you like to say: ')

#logging.debug(input('Press enter to continue!'))

browser = webdriver.Chrome()
browser.get(url)

login_elem = browser.find_element_by_id('identifierId')
login_elem.send_keys(email)
login_elem.send_keys(Keys.ENTER)
time.sleep(3)

### Xpath= //tagname[@attribute='value']

Xpath= "//input[@type='password']"


password_elem = browser.find_element_by_css_selector('.whsOnd.zHQkBf')
logging.debug(password_elem.tag_name)
logging.debug(type(password_elem))


password_elem.send_keys(password)
password_elem.send_keys(Keys.ENTER)
time.sleep(5)

email_compose_button = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3')
email_compose_button.click()
time.sleep(3)

email_recipient_form = browser.find_element_by_css_selector('textarea.vO')
email_recipient_form.send_keys(email_recipient)

email_subject = browser.find_element_by_css_selector('.aoT')
logging.debug(email_subject.tag_name)
email_subject.send_keys('This Email is sent from my Python Script')
time.sleep(1)

email_body = browser.find_element_by_css_selector('div.Am.Al.editable.LW-avf')
email_body.send_keys(body)
time.sleep(1)

email_send_button = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.aoO.T-I-atl.L3')
email_send_button.click()
time.sleep(5)

#time.sleep(2)
browser.quit()

print('Done, email sent!')
