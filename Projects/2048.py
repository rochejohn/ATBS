#! /usr/bin/env python3


'''
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with
the arrow keys. You can actually get a fairly high score by repeatedly sliding in an up, right, down,
and left pattern over and over again. Write a program that will open the game at
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left
keystrokes to automatically play the game.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging,time

logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def play_game():

    print('\nWelcome to the Game 2048, the automated version!\n\n')
    input('Please press enter to begin the game!')

    browser = webdriver.Chrome()
    browser.get('https://gabrielecirulli.github.io/2048/')
    game_elem = browser.find_element_by_tag_name('html')
    logging.debug(game_elem.tag_name)
    logging.debug(game_elem)

    game_over_elem = browser.find_element_by_css_selector('div.game-container > div > p')
    game_score_elem = browser.find_element_by_css_selector('div.score-container')




    while True:

        game_elem.send_keys(Keys.UP)
        game_elem.send_keys(Keys.RIGHT)
        game_elem.send_keys(Keys.DOWN)
        game_elem.send_keys(Keys.LEFT)


        if game_over_elem.text == 'Game over!':
            break

    final_score = game_score_elem.text
    print('The Game is now finished, your score is: ' + final_score + '!')
    browser.quit()

play_game()




while True:

    ans = input('\nWould you like to play again? (y/n): ')

    if ans.lower() == 'y':
        play_game()
    elif ans.lower() == 'n':
        print('Goodbye')
        break
    else:
        print('Invalid Selection!')
