# 	First we need out libraries to handle the scraping. First, requests
import requests
# 	We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# 	We will also need sys to handle argument manipulation
import sys

item = "item"
# url = "https://www.amazon.com"

#	If there are any spaces in the search string somehow, fix them now
item = "+".join(item.split())

#	Next, we need the search URL. Try searching something generic on the website
#	to find it. For Amazon, it's this:
url = "http://www.amazon.com/s?url=search-alias%3Daps&field-keywords=" + item

#	We use that url to get a request from the website
#	At this point, we will have the entire web page of the search to parse!
r = requests.get(url)

#	Create a soup object from that request
#	This will make it easier to search for stuff
soup = bsoup(r.text, "html.parser")



#	Bonus test stuff I was working work to see if I was getting the url right.
		# print r.text.encode('utf-8')
		# print r.url