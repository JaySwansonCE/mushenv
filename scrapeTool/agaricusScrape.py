import csv
import urllib.request

from bs4 import BeautifulSoup
from lxml import html
import requests


allLinks = []
reader = csv.reader(open("data3.csv"), delimiter="\n")
for x in reader:
	allLinks.append(str(*x))	

linkOne = allLinks[0]
print(linkOne)
page = urllib.request.urlopen(linkOne)
myBytes = page.read()
mystr = myBytes.decode("utf8")
page.close()

print(mystr)
