'''
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program has several bugs in it.
Run through the program a few times to find the bugs that keep the program from working correctly.
'''

import random,logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # uncomment/comment to disable/enable logging messages


import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

coin_sides_dict={0:'tails',1:'heads'} #created dictionary to match toss int to heads or tails

toss = coin_sides_dict[random.randint(0, 1)] # 0 is tails, 1 is heads

logging.debug('The toss value is ' + str(toss)) # debug line to show current value

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input() #removed additional s for guesss
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')