# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
# url = 'http://python-data.dr-chuck.net/comments_42.html'
# url = 'http://python-data.dr-chuck.net/comments_349434.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
print 'Count', len(tags)
print 'Sum', sum(int(tag.contents[0]) for tag in tags)
