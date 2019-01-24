'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting images.
You could write a program that works with any photo site that has a search feature.
'''


'''
Will use imgur site
Allow user to search for own category
creates folder imgur-downloads
Create sub-folder to download up to 10 images only (set limit)
Example to be used (Dog Memes from Imgur)
'''
#####SWITCHING TO SELENIUM AS REQUESTS WONT LOAD JS AND TAGS NOT FOUND IN BS4

### FINISHED UPDATE: Could use Selenium and the use requests with selenium (.page_source)
### Then bs4 to get element of full size image
### requests to download full image and iter_content to save

#Instead
### All thumbnail images are same as full size with extra 'b' at end.
### used string splicing to change links and download using only requests and bs4

from selenium import webdriver

import logging,bs4,requests,os
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.CRITICAL)
print('''
Welcome to Imgur download!

Please enter the catagory you would like to download!

Limited to 10 downloads

Images will be stored in the current working directory under a folder named after your search topic!
''')

user_input= input('Please enter topic: ')
print('\nWorking... Please wait....')

imgur_search = requests.get('https://imgur.com/search?q=' + user_input)

soup_imgur_search = bs4.BeautifulSoup(imgur_search.text,features="html.parser")

elem = soup_imgur_search.select('a.image-list-link img')

logging.debug(len(soup_imgur_search))

search_num = min(10,len(elem))
logging.debug(search_num)

os.makedirs(os.path.join('Imgur-Downloads',user_input),exist_ok=True)

for num in range(search_num):

    try:
        logging.debug(elem[num].get('src'))

        unmod_link = elem[num].get('src')
        mod_link = 'https://' + unmod_link[2:-5] + unmod_link[-4:]
        logging.debug(mod_link)

        final_image = requests.get(mod_link)
        logging.debug(os.path.basename(mod_link))

        print('Downloading Image: ' + mod_link)


        playfile = open(os.path.join('Imgur-Downloads',os.path.join(user_input,os.path.basename(mod_link))),'wb')
        for chunk in final_image.iter_content(100000):
            playfile.write(chunk)
        playfile.close()

        print('Successfully saved as ' + os.path.basename(mod_link))
        print()

    except:
        print('\n\nAn unidentified issue occured.\nMoving to next file.\n\n')
        continue