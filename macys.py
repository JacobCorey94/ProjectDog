import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

def macys(item):
        print "macys"
        item = item.replace(" ", "-")
        url = "https://www.macys.com/shop/featured/" + item
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        r = requests.get(url, headers=headers)
        soup = bsoup(r.text, "html.parser")

        prodlist = []
        raw = []
        
        expr = "\$\d*\.\d{2}"
        linkexpr = "(?<=href=\")(\/\S+)(?=\")"
        c = 0
        for li in soup.find_all('li', class_='productThumbnail borderless'):
                raw.append(str(li))
                
                prodlist.append([])
                prodlist[c].append(li.find(class_='shortDescription').text.replace("\n",""))
                prodlist[c].append(re.findall(expr, raw[c])[len(re.findall(expr,raw[c]))-1][1:])
                
                prodlist[c].append("https://www.macys.com" + re.findall(linkexpr, raw[c])[0])

                c = c + 1

        # return results
        if len(prodlist) == 0:
                return ["Empty"]
        return prodlist
