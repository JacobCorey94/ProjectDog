import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

def staples(item):
	#item = "usb charger"
	print "staples"
	item = item.replace(" ", "%2520")
	url = "http://www.staples.com/fillertext/directory_" + item
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

	r = requests.get(url, headers=headers)
	soup = bsoup(r.text, "lxml")

	prodlist = []
	raw = []

	expr = "\$\d*\.\d{2}"
	linkexpr = "(\/\S+)(?=\")"

	c = 0
	for div in soup.find_all('div', class_='stp--new-product-tile-container desktop'):
		raw.append(str(div))

		prodlist.append([])
		prodlist[c].append(div.find("a", class_='product-title scTrack pfm').text.strip())
		prodlist[c].append(re.findall(expr, raw[c])[0][1:])
		prodlist[c].append("https://www.staples.com" + re.findall(linkexpr, raw[c])[0])

		c = c + 1

	if len(prodlist) == 0:
		#print "STAPLES IS EMPTY!"
		prodlist.append("Empty")
		#print "index 0 is: " + prodlist[0]

	return prodlist

# for i in prodlist:
# 	print i[0]
# 	print i[1]
# 	print i[2]