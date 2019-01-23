'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting images.
You could write a program that works with any photo site that has a search feature.
'''


'''
Will use imgur site
Allow user to search for own category
Create folder to download up to 10 images only (set limit)
Example to be used (Dog Memes from Imgur)
Can use Selenium or Requests/BS4 
Using BS4 so no browser needs to be opened!
'''


'''os for making dir and os path for file paths and names'''
'''requests to download html page, and images'''
'''bs4 to parse and search for html elements, next button and images'''

import logging, os, requests, bs4

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#TODO change below to variable so user can enter own search
request_imgur_home_page = requests.get('https://imgur.com/search?q=dog%20meme')        # make request object for imgur homepage
request_imgur_home_page.raise_for_status()                         # check if any issues getting page

soup_imgur = bs4.BeautifulSoup(request_imgur_home_page.text,features='html.parser')       # create the bs4 object from the requests objects attribute text(where html text is stored as a string)

soup_elem = soup_imgur.select('d > a')

logging.debug(type(soup_elem))
logging.debug(len(soup_elem))
logging.debug(soup_elem[0])

logging.debug(request_imgur_home_page.text[0:200])