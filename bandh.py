import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

# def bandh(item):

print "starting"
item = "sd card"
item = item.replace(" ", "%20")
print item
url = "https://www.bhphotovideo.com/bnh/controller/search?Ntt=" + item

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = bsoup(r.text, "lxml")

prodlist = []
raw = []

expr = "\$\d*\.\d{2}"
linkexpr = "(https:\/\/www\.bhphotovideo\.com\/c\/product\/\S+)(?=\")"
c = 0	
for div in soup.find_all('div', class_='item clearfix js-item  js-bhItemObj'):
	print "Found list item!"
	raw.append(str(div))
	
	prodlist.append([])
	prodlist[c].append(div.find('span', itemprop="brand").text.strip() + " " + div.find('span', itemprop="name").text.strip())
	print div.find('span', itemprop="brand").text.strip() + " " + div.find('span', itemprop="name").text.strip()
	prodlist[c].append(re.findall(expr, raw[c])[0])
	print re.findall(expr, raw[c])[0]
	prodlist[c].append(re.findall(linkexpr, raw[c])[0])
	print re.findall(linkexpr, raw[c])[0]

	c = c + 1

	# if len(prodlist) == 0:
	# 	prodlist.append("Empty")
	# return prodlist

# for i in bandh("sd card"):
# 	print i[0]
# 	print i[1]
# 	print i[2]