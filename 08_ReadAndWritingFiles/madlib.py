f = open('./madlib.txt', 'r+')

typesOfWord = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']

#filedata = f.read()

for line in f:
    for word in line.split():
        if word in typesOfWord:
           newWord = input('enter a ' + word + " ")
           f = f.replace(word, newWord)


f.close()

        

#contents = madlibs.read()
#print(contents)