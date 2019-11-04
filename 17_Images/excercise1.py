from PIL import Image

# opens image and also resaves it from a .jpg to a .png
def ex1():
    catIm = Image.open('2019_07_29.jpg')

    print(catIm.size)

    catIm.save('new.png')
#ex1()

# creates purple and transparent images
def ex2():
    im = Image.new('RGBA', (100,200), 'Purple')

    im.save('purple.png')

    im2 = Image.new('RGBA', (20,20))

    im2.save('TransparentImage.png')


# crops a rectangle at the given passed coordinates
def ex3():
    catIm = Image.open('2019_07_29.jpg')
    croppedIm = catIm.crop((335, 345, 565, 560))
    croppedIm.save('cropped.png')

