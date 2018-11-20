import csv

from bs4 import beautifulsoup
from lxml import html
import requests


allLinks = []
reader = csv.reader(open("data3.csv"), delimiter="\n")
for x in reader:
	allLinks.append(x)	

print(allLinks(0))