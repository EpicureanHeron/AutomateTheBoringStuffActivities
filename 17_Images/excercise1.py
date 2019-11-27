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
    catIm = Image.open('Zophie.png')
    croppedIm = catIm.crop((335, 370, 565, 550))
    croppedIm.save('cropped2.png')


# copies a cropped image of cat's face, then pastes it at specific coordinates, and then saves it. 
def ex4():
    catIm = Image.open('zophie.png')
    catCopyIm = catIm.copy()

    faceIm = catIm.crop((335, 345, 565, 560))
    print(faceIm.size)

    catCopyIm.paste(faceIm, (0, 0))
    catCopyIm.paste(faceIm, (400, 500))
    catCopyIm.save('pasted.png')

def ex5():
    catIm = Image.open('zophie.png')
    #assigning two variables based on the return from catIm.size
    catImWidth, catImHeight = catIm.size
    faceIm = catIm.crop((335, 345, 565, 560))
    faceImWidth, faceImHeight = faceIm.size
    catCopyTwo = catIm.copy()

    for left in range(0, catImWidth, faceImWidth):
        for top in range(0, catImHeight, faceImHeight):
            print(left, top)
            catCopyTwo.paste(faceIm, (left, top))

    catCopyTwo.save('tiled.png')

# resizing images, stretching and shrinking
def ex6():
    catIm = Image.open('zophie.png')
    width, height = catIm.size
    quatersizedIm = catIm.resize((int(width/2), int(height/2)))
    quatersizedIm.save('quarterportion.png')
    svelteIm = catIm.resize((width, height + 300))
    svelteIm.save('svelte.png')

    thiccIm = catIm.resize((width + 600, height))
    thiccIm.save('thicc.png')




def ex7():
    catIm = Image.open('zophie.png')
    # catIm.rotate(90).save('rotated90.png')
    # catIm.rotate(180).save('rotated180.png')
    # catIm.rotate(270).save('rotated270.png')
    #catIm.rotate(6, expand=True).save('rotated6_expanded.png')
    catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

ex7()