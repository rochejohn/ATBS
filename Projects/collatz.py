#! /usr/bin/env python3


def collatz(number):



    if number % 2 == 0:
        print(number // 2)
        return number // 2

    else:
        return 3 * number + 1



def game():

    try:
        number = int(input('Please enter a number: '))
        while number != 1:
            number = collatz(number)
        play()

    except ValueError:
        print('Please enter a valid number!')
        game()

def play():
    ans = input('Try again? Y or N:\n').upper()

    if ans == 'Y':
        game()

    elif ans == 'N':
        print('GoodBye!')

    else:
        print('Invalid Option')
        play()

game()
