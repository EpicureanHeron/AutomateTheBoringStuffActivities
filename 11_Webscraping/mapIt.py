#! python3
# mapIt.py - Launches ma in broweser using address from command line

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from command l ine
    address = ' '. join(sys.argv[1:])


else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)