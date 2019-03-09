import bs4, sys, webbrowser, requests

if len(sys.argv) > 1:
    # get address from command l ine
    search = ' '. join(sys.argv[1:])


url = 'https://www.google.com/search?q=%s&ie=utf-8&oe=utf-8' %(search)


res = requests.get(url)
res.raise_for_status()
searchResults = bs4.BeautifulSoup(res.text, 'html.parser')

linkElem = searchResults.select('.r a')

for x in linkElem:
    link = x.get('href')
    #print(link)
    #print('')
    webbrowser.open('http://google.com'+link)