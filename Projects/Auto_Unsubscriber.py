'''

Write a program that scans through your email account, finds all the unsubscribe links in all your emails,
and automatically opens them in a browser. This program will have to log in to your email provider’s
IMAP server and download all of your emails. You can use BeautifulSoup (covered in Chapter 11)
to check for any instance where the word unsubscribe occurs within an HTML link tag.

Once you have a list of these URLs, you can use webbrowser.open() to automatically open all of these links in a browser.
You’ll still have to manually go through and complete any additional steps to
unsubscribe yourself from these lists.

'''

# use imapclient to get email
# use pyzmail to get html/text this case html
# beautiful soup to get tags with unsubscribe link
# webbrowser.open to open the links

# had to install ssl certs on python mac

# had to change google login to allow login from less secure apps setting

import imapclient,pyzmail,bs4,webbrowser,sys
import pprint

try:

    print('\nWelcome to Email unsub!! (Gmail users only)\n')

    user_email = input('Please enter your email address: ')

    password = input('Please enter your password: ')


    imap_obj = imapclient.IMAPClient('imap.gmail.com',ssl=True)

    imap_obj.login(user_email,password)

except:
    sys.exit('\nThere was a issue with your email or password!\nExiting!')


imap_obj.select_folder('INBOX',readonly=True)

uids = imap_obj.search(['SINCE', '01-JAN-2019'])

print('\nChecking ' +str(len(uids)) + ' emails!!')

email_count = 1

print('\nListing emails with unsubscribe links:\n')

for email in uids:



    rawMessage = imap_obj.fetch([email], ['BODY[]'])
    #pprint.pprint(rawMessage)

    message = pyzmail.PyzMessage.factory(rawMessage[email][b'BODY[]'])

    if message.html_part == None:
        continue


    sender_info =  message.get_addresses('from')

    sender_name = sender_info[0][0]
    sender_email = sender_info[0][1]




    pyzmail_mail_html = message.html_part.get_payload().decode(message.html_part.charset)

    bs4_soup_obj = bs4.BeautifulSoup(pyzmail_mail_html, "html.parser")

    tag_objs = bs4_soup_obj.select('a')



    for tag in tag_objs:
        if 'unsub' in tag.getText().lower():
            webbrowser.open(tag.get('href'))
            print('Email #' + str(email_count) + ' Subject: '  + message.get_subject())
            print('From: ' + sender_name + ', ' + sender_email)
            print()


            email_count += 1

print('\nAll unsub links have been found and opened in the browser, please unsub from each!')

    #print(message.get_addresses('from'))
    #print(message.get_addresses('to'))

    #print(message.text_part != None)
    #print(message.text_part.get_payload().decode(message.text_part.charset))

    #print(message.html_part != None)
    #print(message.html_part.get_payload().decode(message.html_part.charset))

