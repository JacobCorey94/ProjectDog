import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

def walmart(item):
	#item = "usb charger"
	print "Walmart"
	item = item.replace(" ", "%20")
	url = "https://www.walmart.com/search/?query=" + item
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

	r = requests.get(url, headers=headers)
	soup = bsoup(r.text, "lxml")

	prodlist = []
	raw = []

	# expr = "\$\d*\.\d{2}"
	linkexpr = "(\/\S+)(?=\")"

	c = 0
	for div in soup.find_all('div', class_='search-result-listview-item clearfix'):
		raw.append(str(div))

		prodlist.append([])
		prodlist[c].append(div.find("span", class_='visuallyhidden').text.strip())
		prodlist[c].append(div.find("span", class_='Price-characteristic').text.strip() + "." + div.find("span", class_='Price-mantissa').text.strip())
		prodlist[c].append("https://www.walmart.com" + re.findall(linkexpr, raw[c])[0])

		c = c + 1

	if len(prodlist) == 0:
		return ["Empty"]
	return prodlist

# for i in prodlist:
# 	print i[0]
# 	print i[1]
# 	print i[2]