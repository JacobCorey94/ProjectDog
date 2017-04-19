import requests
from bs4 import BeautifulSoup as bsoup
import sys
import re

def newegg(item):
        final = []
        while len(final) == 0:
                try:
                        print "newegg"
                        item = item.replace(" ", "+")
                        
                        url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=" + item
                        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

                        r = requests.get(url, headers=headers)

                        soup = bsoup(r.text, "html.parser")

                        prodlist = []
                        raw = []

                        expr = "\$\d*\.\d{2}" 
                        linkexpr = "(https:\/\/www\.newegg\.com\/\S+)(?=\")" 
                        c = 0   # Counter = 0
                        for li in soup.find_all('div', class_='item-container '):
                                raw.append(str(li))
                                prodlist.append([])
                                prodlist[c].append(li.find("a", class_="item-title").text)
                                price = li.find("li", class_="price-current").text
                                prodlist[c].append(re.findall(expr, price)[0][1:])
                                prodlist[c].append(re.findall(linkexpr, raw[c])[0])
                                c = c + 1

                        final += prodlist
                        if len(final) == 0:
                                return ["Empty"]
                        return final
                except:
                        pass

# for i in newegg("item"):
#         print i[0]
#         print i[1]
#         print i[2]
