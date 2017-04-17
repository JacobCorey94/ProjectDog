import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

item = "usb charger"

item = item.replace(" ", "%20")
url = "https://www.walmart.com/search/?query=" + item
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = bsoup(r.text, "lxml")

prodlist = []
raw = []

expr = "\$\d*\.\d{2}"

c = 0
for div in soup.find_all('div', class_='search-result-listview-item clearfix'):
	raw.append(str(div))

	prodlist.append([])
	prodlist[c].append(div.find("span", class_='visuallyhidden').text.strip())
	prodlist[c].append(re.findall(expr, raw[c])[0])