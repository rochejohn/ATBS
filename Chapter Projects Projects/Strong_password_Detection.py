'''
Chapter 7


Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and
lowercase characters, and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.

'''


import re, time


while True:


    print('''
Hello,
    
Welcome to the Strong Password Detection Test.
    
Please note:
    
A strong password is defined as one that is at least eight characters long, contains both uppercase and
lowercase characters, and has at least one digit.
    
If you would like to check if you password meets the security requirements please
enter you password below.''')

    password = input('Password: ')

    print('\nTesting your password now.\nPlease wait .',end = ' ')
    time.sleep(1.5)
    print('.',end = ' ')
    time.sleep(1.5)
    print('.',end=' ')
    time.sleep(1.5)
    print('.',end=' ')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print()

    check_lower_case = re.compile(r'[a-z]')
    check_higher_case = re.compile(r'[A-Z]')
    check_num = re.compile(r'\d+')

    has_lower = check_lower_case.search(password)
    has_higher = check_higher_case.search(password)
    has_num = check_num.search(password)

    if len(password) >= 8:

        if has_lower != None:

            if has_higher != None:

                if has_num != None:
                    print('Well Done! Your password meets the security requirements!')


                else:
                    print('Password must contain at least one number!!')


            else:
                print('Password must contain higher case character!!')


        else:
            print('Password must contain lower case character!!')


    else:
        print('Password needs to be at least 8 characters long!')


    ans = input('Would you like to try again? (y/n): ')


    if ans == 'y':
        continue


    elif ans == 'n':
        print('Goodbye!')
        break


    else:
        print('Invalid Option! Default is yes!')







