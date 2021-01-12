import bs4
import handlerFuncs as handler
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

class InputError(Exception):
	pass

def main():
	
	handleDups = input("How should duplicates be handled?: ")
	#catch and raise exception
	handlerBool = True if handleDups == "highest" else False
	
	myUrl = "https://www.microcenter.com/search/search_results.aspx?N=4294966937&NTK=all&sortby=match&rpp=96"


	client = uReq(myUrl)
	page = client.read()
	client.close()
	pageSoup = soup(page,"html.parser")

	#each item is a product wrapper
	containers = pageSoup.findAll("li",{"class":"product_wrapper"})

	#stores item/price pairs in this dictionary
	itemsDict = {}


	for containerItem in containers:
		brand = containerItem.div.find('a',{"class":"image"})["data-brand"]
		name = containerItem.div.find('a',{"class":"image"})["data-name"]
		name = brand + " " + name
		price = containerItem.div.find('a',{"class":"image"})["data-price"]
		#if item is already in dictionary -> dictionaries have unique keys so have to find cheaper item
		if name in itemsDict.keys():
			if handlerBool:
				handler.handlerHigh(itemsDict,name,price)
			else:
				handler.handlerLow(itemsDict,name,price)
		else:
			itemsDict[name]=price

	for key,value in itemsDict.items():
		print(f"GPU: {key} -> Price: {value}")

while True:
	try:
		main()
		break
	except InputError:
		print('Error: The prompt only takes in responses -- "highest" and "lowest"')