import re

def passwordDetection(pw):

    alphaLengthRegex = re.compile(r'^[A-z][0-9]{1,8}$')

    mo1 = alphaLengthRegex.search(pw)
    print(mo1.group())
   
passwordDetection('Test4')
#passwordDetection('')
passwordDetection('BLahBlahB')