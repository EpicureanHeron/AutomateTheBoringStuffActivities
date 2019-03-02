import os, shutil, re


def selectiveCopy(fileExt):

    # need to add regex to say AFTER the '.' in the file name, check to see if it matches the characters pased by user via fileExt.
    directory = os.path('./')


    for folderName, subfolders, filenames in os.walk(directory):
        print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

userFileExt = input("enter the file extension (this will be the part after the '.' such that spam.txt would be 'txt'): ")



selectiveCopy(userFileExt)