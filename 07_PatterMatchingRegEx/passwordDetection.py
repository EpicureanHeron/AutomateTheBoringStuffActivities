import re

def passwordDetection(pw):

    alphaCaps = re.compile(r'[a-z]{1,8}')
    alphaSmall = re.compile(r'[A-Z]{1,8}')
    numberRe = re.compile(r'[0-9]{1,8}')

    mo1 = alphaCaps.search(pw)
    mo2 = alphaSmall.search(pw)
    mo3 = numberRe.search(pw)

    if mo1 == None or mo2 == None or mo3 == None or len(pw) > 8:
        print(pw + " is not secure")

    else:
        print(pw + " is secure")

   
passwordDetection('Test4')
passwordDetection('1')
passwordDetection('Eight555')
#passwordDetection('')
passwordDetection('BLahBlahB000')