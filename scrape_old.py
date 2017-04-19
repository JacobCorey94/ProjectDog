# 	First we need out libraries to handle the scraping. First, requests
import requests
# 	We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# 	We will also need sys to handle argument manipulation
import sys
#	For some, APIs were able to be used. json is needed
import json
#	using regular expressions is helpful for scraping specific strings
import re

# 	This is the Amazon.com function.
# 	It handles the scraping of Amazon
# 	EACH WEBSITE WILL HAVE ITS OWN FUNCTION (located in its own .py file)!
import amazon
import bestbuy
import staples
import macys
import walmart
import homedepot
import target

#	This is the main function
# 	Parameters: item_to_search_for websiteURL1 websiteURL2 etc.
# 	Parameters are stored as a tuple to parse through
def scrape(arg):
	master = []			#	Master stores ALL RESULTS
	amazonlist = []		#	Holds amazon results
	stapleslist = []
	macyslist = []
	walmartlist = []
	homedepotlist = []

	#	Amazon does NOT use API, and thus might fail occaisionally. Try look fixes this
	if "amazon" in arg:
		while len(amazonlist) == 0:
			try:
				amazonlist = amazon.amazon(arg[1]) # arg[1] should ALWAYS BE THE ITEM to search for
				if amazonlist[0] == "Empty":
					print "amazon returned no results"
				else:
					master += amazonlist
			except:
				pass

	#	Bestbuy DOES use API. I would suggest using API, as its faster and more reliable
	#	However, you will need to get an API key from the website for this
	if "bestbuy" in arg:
		master += bestbuy.bestbuy(arg[1])

	# ADD MORE FUNCTION CALLS TO OTHER SITES HERE!!!!!!!
	#if "https://wherever.net" in arg:
		#wherever(arg[1])

	# I have had zero issues with staples, but let's not take a chance...
	if "staples" in arg:
		while len(stapleslist) == 0:
			try:
				stapleslist = staples.staples(arg[1])
				print stapleslist[0]
				if stapleslist[0] == "Empty":
					print "Staples returned no results"
				else:
					master += stapleslist
			except:
				pass

	if "macys" in arg:
		while len(macyslist) == 0:
			try:
				macyslist = macys.macys(arg[1])
				if macyslist[0] == "Empty":
					print "Macy's returned no results"
				else:
					master += macyslist
			except:
				pass

	if "walmart" in arg:
		while len(walmartlist) == 0:
			try:
				walmartlist = walmart.walmart(arg[1])
				if walmartlist[0] == "Empty":
					print "Walmart returned no results"
				else:
					master += walmartlist
			except:
				pass

		master += walmartlist

	if "homedepot" in arg:
		while len(homedepotlist) == 0:
			try:
				homedepotlist = homedepot.homedepot(arg[1])
				if homedepotlist[0] == "Empty":
					print "homedepot returned no results"
				else:
					master += homedepotlist
			except:
				pass
		master += homedepotlist

	if "target" in arg:
		master += target.target(arg[1])

	# print json.dumps(master)
	for i in master:
		print i[0]
		print i[1]
		print i[2]
		
	#	More tests inside the function to make sure the arguments were passed in correctly

	# print "scrape was called with", len(arg), "arguments:",

	# for x in arg:
	# 	print x,
	# print ""

	# return "You made it into the scrape() function!"

# 	If the input is wrong, print the error to the results page
# 	Otherwise, call the scrape() function
if len(sys.argv) < 3:

	print "ERROR! Wrong arguments passed in, 0.00"
	print "Proper use: python scrape.py item web1 web2 etc, 0.00"

else:	
	scrape(list(sys.argv))

# 	Output tests to see how arguments were passed in
# 	Feel free to run similar tests to make sure you understand how it's working

# print "This is the name of the script:", sys.argv[0] 
# print "Number of arguments:", len(sys.argv)
# print "The arguments are:", str(sys.argv)
