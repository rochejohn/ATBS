#! /usr/bin/env python3


'''
Extend the multiclipboard program in this chapter so that it
has a delete <keyword> command line argument
that will delete a keyword from the shelf.
Then add a delete command line argument that will delete all keywords.
'''

'''
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
'''



import shelve, sys, pyperclip


clipshelf = shelve.open('mynewshelf')

if len(sys.argv) == 3:

    if sys.argv[1].lower() == 'save':
        clipshelf[sys.argv[2]] = pyperclip.paste()
        print('Saved as {}'.format(sys.argv[2]))

    elif sys.argv[1].lower() == 'delete':
        del clipshelf[sys.argv[2]]
        print('Deleted: {}'.format(sys.argv[2]))

    else:
        print('Invalid option!')

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        #pyperclip.copy(str(list(clipshelf.keys())))
        #print available options to screen instead of copy to clip (better xp)
        print('List contains: {}'.format(list(clipshelf.keys())))

    elif sys.argv[1] in clipshelf.keys():
        pyperclip.copy(clipshelf[sys.argv[1]])
        print('{} now copied to clipboard, paste to see results'.format(sys.argv[1]))

    elif sys.argv[1].lower() == 'delete':
        for key in clipshelf.keys():
            del clipshelf[key]
            print('{} has been deleted'.format(key))
        print('All items have now been deleted!')


    else:
        print('Invalid option!')

clipshelf.close()



