import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
self.soup = bs4(noStarchSoup, 'html.parser')

type(noStarchSoup)
