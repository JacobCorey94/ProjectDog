# 	First we need out libraries to handle the scraping. First, requests
import requests
# 	We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# 	We will also need sys to handle argument manipulation
import sys

# 	This is the Amazon.com function.
# 	It handles the scraping of Amazon
# 	EACH WEBSITE WILL HAVE ITS OWN FUNCTION!

# 	Please add them all otherwise this scraper will not work!

def amazon(item):
	print item

#	This is the main function
# 	Parameters: item_to_search_for websiteURL1 websiteURL2 etc.
# 	Parameters are stored as a tuple to parse through
def scrape(arg):
	if "https://www.amazon.com" in arg:
		amazon(arg[1]) # arg[1] should ALWAYS BE THE ITEM to search for

	# ADD MORE FUNCTION CALLS TO OTHER SITES HERE!!!!!!!
	#if "https://wherever.net" in arg:
		#wherever(arg[1])

	#	More tests inside the function to make sure the arguments were passed in correctly

	# print "scrape was called with", len(arg), "arguments:",

	# for x in arg:
	# 	print x,
	# print ""

	# return "You made it into the scrape() function!"

# 	If the input is wrong, print the error to the results page
# 	Otherwise, call the scrape() function
if len(sys.argv) < 3:

	text_file = open("results.txt", "w")
	text_file.write("ERROR! Wrong arguments passed in, 0.00\n")
	text_file.write("Proper use: python scrape.py item web1 web2 etc, 0.00\n")
	text_file.close();

	print "Error printed to results.txt..."

else:	
	scrape(list(sys.argv))

# 	Output tests to see how arguments were passed in
# 	Feel free to run similar tests to make sure you understand how it's working

# print "This is the name of the script:", sys.argv[0] 
# print "Number of arguments:", len(sys.argv)
# print "The arguments are:", str(sys.argv)