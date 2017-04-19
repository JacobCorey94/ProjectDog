import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

def homedepot(item):
        # item = "item"
        print "homedepot"
        item = item.replace(" ", "%2520")
        url = "http://www.homedepot.com/s/" + item + "?NCNI-5"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

        r = requests.get(url, headers=headers)
        soup = bsoup(r.text, "html.parser")

        prodlist = []
        raw = []

        expr = "\$\d*\.\d{2}"
        linkexpr = "(\/p\/\S+)(?=\")"

        c = 0
        for div in soup.find_all('div', class_='pod-inner'):
                raw.append(str(div))
                #print raw[c]

                prodlist.append([])
                title = div.find("div", class_="pod-plp__description").text
                title = re.sub('\s+', ' ', title).strip()
                prodlist[c].append(title)
                prodlist[c].append(re.findall(expr, raw[c])[0][1:])
                prodlist[c].append("https://www.homedepot.com" + re.findall(linkexpr, raw[c])[0])

                c = c + 1

        if len(prodlist) == 0:
                return ["Empty"]
        return prodlist
