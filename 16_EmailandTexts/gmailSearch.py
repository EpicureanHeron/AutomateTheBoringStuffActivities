import imapclient
import pprint
import imaplib
imaplib._MAXLINE = 10000000
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

email = input('enter email: ')
password = input('password: ')

imapObj.login(email, password)

search = input('enter search criteria:')

UIDs = imapObj.gmail_search(search)

print(UIDs)

# rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

# pprint.pprint(rawMessages)
