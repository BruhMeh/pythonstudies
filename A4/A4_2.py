import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
numCycles = int(raw_input('Enter Count: '))
numPosition = int(raw_input('Enter Position: '))
# url = 'http://python-data.dr-chuck.net/known_by_Fikret.html '
# url = 'http://python-data.dr-chuck.net/known_by_Colm.html '
# numCycles = 7
# numPosition = 18

count = 0

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('a')

while (count < numCycles):
    if(count == 0):
        print 'Retrieving:', url
        html = urllib.urlopen(url).read()
    else:
        print 'Retrieving:', tags[numPosition-1].get('href', None)
        html = urllib.urlopen(tags[numPosition-1].get('href', None)).read()

    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    count+=1

print 'Name', tags[numPosition-1].contents[0]
