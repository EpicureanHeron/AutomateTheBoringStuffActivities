f = open('./madlib.txt', 'r+')

typesOfWord = ['ADJECTIVE', 'NOUN', 'VERB.', 'ADVERB']

#filedata = f.read()

newFile = ''

for line in f:
    for word in line.split():
        if word in typesOfWord:
           newWord = input('enter a ' + word + ": ")
           newFile += newWord + ' '
        
        else:
                newFile += word + ' '
                
f.truncate(0) 
print(newFile)          
f.write(newFile)
print

f.close()

        

#contents = madlibs.read()
#print(contents)