from __future__ import print_function
import sys
import operator
import csv

def reverseCsv():
	print('Reversing list...')
	reader = csv.reader(open("data1.csv"), delimiter=",")

	sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False) #reverses the list order
	sortedlist.pop() #Removes the last item in the list

	myFile = open('data2.csv', 'w')
	with myFile:  
   		writer = csv.writer(myFile)
   		writer.writerows(sortedlist)

def ammendLink():
	print('Ammending Links...')
	fullLink = []
	reader = csv.reader(open("data2.csv"), delimiter="\n")
	for x in reader:
		fullLink.append(['www.wikipedia.com' + str(*x)])
	print(fullLink)

	myFile = open('data3.csv', 'w')
	with myFile:  
   		writer = csv.writer(myFile)
   		writer.writerows(fullLink)	
	
reverseCsv()
ammendLink()
print("DONE")
