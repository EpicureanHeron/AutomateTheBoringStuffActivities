import requests, bs4, os, threading

url = 'http://xkcd.com/'

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        # download the page
        print("downloading page http://xkcd.com/%s..." % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text) 

        # find the url for the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('could not find comic image')
        else:
            comicUrl = comicElem[0].get('src')
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')