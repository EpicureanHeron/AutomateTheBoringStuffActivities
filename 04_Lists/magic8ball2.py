import random

messages = ['It is certain',
'It is decidedly so',
'Yes defintely',
'Reply hazy try again',
'Ask again later',
'Concetrate and ask again',
'My reply is no',
'Outlook not so good', 
'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])