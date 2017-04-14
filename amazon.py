# 	First we need out libraries to handle the scraping. First, requests
import requests
# 	We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# 	We will also need sys to handle argument manipulation
import sys

item = "item"
# url = "https://www.amazon.com"

#	If there are any spaces in the search string somehow, fix them now
item = item.replace(" ", "+")

#	Next, we need the search URL. Try searching something generic on the website
#	to find it. For Amazon, it's this:
url = "http://www.amazon.com/s?url=search-alias%3Daps&field-keywords=" + item

#	We use that url to get a request from the website
#	At this point, we will have the entire web page of the search to parse!
r = requests.get(url)

#	Create a soup object from that request
#	This will make it easier to search for stuff
soup = bsoup(r.text, "lxml")

# if "href" in soup.find("div", {"class": "a-row a-spacing-none"}).prettify():
# 	print "found a URL"
# else:
# 	print "No URL found :'("

# for link in soup.findAll("div"):
# print link


urllist = []	#Stores ALL URLs on the page
prodlist = []	#Stores only the product URLs
spanlist = []	#Stores the <span></span> that includes the price
pricelist = []	#Stores the prices of the products

#	Grab the search results of the page itself
#	THIS IS DEPENDENT ON THE WEBSITE ITSELF, SO SEARCH WITH SEARCH ELEMENT IN YOUR BROWSER
for a in soup.find_all('a', href=True):
	if 
	urllist.append(a['href'])

for span in soup.find_all('span'):
	if "<sup class=\"sx-price-currency\">" in str(span):
		spanlist.append(str(span))

# for x in urllist:
# 	print x

#	urllist now has EVERY URL from the page
#	We need to filter out JUST the links to products
for x in urllist:
	if "https://www.amazon.com/" in x and "/dp/" in x and "#" not in x and x not in prodlist:
		prodlist.append(x)

# Quick Python Tip:
# neato = "This is a string"
# neato[3:] will give you "Thi"
# neato.index('i') will return 2? RTFM
# neato[neato.index('i'):]

for y in spanlist:
	if "<sup class=\"sx-price-currency\">" in y:
		#print y
		price = str(y[y.index("<sup class=\"sx-price-currency\">")+len("<sup class=\"sx-price-currency\">"): y.index("</sup>")])
		price += str(y[y.index("sx-price-whole\">")+len("sx-price-whole\">"):y.index("</span>")])
		price += "."
		price += str(y[y.index("<sup class=\"sx-price-fractional\">")+len("<sup class=\"sx-price-fractional\">"):y.index("<sup class=\"sx-price-fractional\">")+len("<sup class=\"sx-price-fractional\">")+2])
		pricelist.append(price)
		#print price

#	ISSUE: Amazon scraping has given me duplicates of every price. Let's fix this
for x in range(len(pricelist),-1,-1):
	if x % 2 == 1:
		pricelist.pop(x)

for z in pricelist:
	print z
for z in prodlist:
	print z

if len(prodlist) == len(pricelist):
	print "YES!"
# for prod in prodlist:
# 	print "Found product:" + prod

# part = results[results.find("s-result-item celwidget")+len("s-result-item celwidget"):results.find("</div>")+len("</div>")]
# url = str(results[results.find("href=\"")+len("href=\""):results.find("\"title")+len("\"title")])
# urllist.append()

# print url
#for soup.find
	#urllist.append("".join(link.prettify().split()))



#	Bonus test stuff I was working work to see if I was getting the url right.
#	print r.text.encode('utf-8')
		# print r.url