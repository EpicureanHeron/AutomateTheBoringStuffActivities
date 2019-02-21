import os, shutil


def selectiveCopy(fileExt):

    directory = os.path('./')

    for folderName, subfolders, filenames in os.walk(directory):
        print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)







userFileExt = input("enter the file extension (this will be the part after the '.' such that spam.txt would be 'txt'): ")

selectiveCopy(userFileExt)