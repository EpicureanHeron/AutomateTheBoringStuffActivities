def commaCode(parameter):
    # parameter.insert(-1, "and")
    listString = ", ".join(parameter)
    lengthOfLastIndex = len(parameter[-1])
    newString = listString[0: (len(listString) - lengthOfLastIndex)] + "and " + listString[(len(listString) - lengthOfLastIndex ) : len(listString)]


    return newString

spam = ['apples', 'bananas', 'tofu', 'cats']

print commaCode(spam)

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print commaCode(messages)