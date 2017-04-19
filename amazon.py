#	First we need out libraries to handle the scraping. First, requests
import requests
# 	We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# 	We will also need sys to handle argument manipulation
import sys
#	using regular expressions is helpful for scraping specific strings
import re

def amazon(item):
	final = []
	while len(final) == 0:
		try:
			#item = "item"
			# url = "https://www.amazon.com"
			print "amazon"
			#	If there are any spaces in the search string somehow, fix them now
			item = item.replace(" ", "+")

			#	Next, we need the search URL. Try searching something generic on the website
			#	to find it. For Amazon, it's this:
			url = "https://www.amazon.com/s?url=search-alias%3Daps&field-keywords=" + item

			#	This isn't always necessary, but sometimes 503 errors will happen without a header.
			#	Better safe than sorry
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

			#	We use that url to get a request from the website
			#	At this point, we will have the entire web page of the search to parse!
			r = requests.get(url, headers=headers)

			#	Create a soup object from that request
			#	This will make it easier to search for stuff
			soup = bsoup(r.text, "lxml")

			prodlist = []	#	Stores the final results
			raw = []		#	Used for temporary html data down below

			#	THIS will differ from site to site. Use inspect element to determine how best to rip results
			#	Double check all results found for what's on the page. Results must be accurate!

			expr = "\$\d*\.\d{2}" 	#	Regular expression for finding references to a price
			linkexpr = "(https:\/\/www\.amazon\.com\/\S+)(?=\")"	#	Regular expression for finding links to amazon products
			c = 0	# Counter = 0
			for li in soup.find_all('li', class_='s-result-item celwidget '):
				# print "Found a list item"
				raw.append(str(li))
				
				prodlist.append([])
				prodlist[c].append(li.find("h2").next_element.strip())
				
				prodlist[c].append(re.findall(expr, raw[c])[0][1:])
				
				prodlist[c].append(re.findall(linkexpr, raw[c])[0])

				# Counter++
				c = c + 1

			# return results
			final += prodlist
			if len(final) == 0:
				#print "AMAZON EMPTY"
				return ["Empty"]
			else:
				return final
		except:
			pass

# for i in amazon(sys.argv[1]):
# 	print i[0]
# 	print i[1]
# 	print i[2]