# First we need out libraries to handle the scraping. First, requests
import requests
# We also need BeautifulSoup from bs4. I'm naming it bsoup to make it easier to type out later on
from bs4 import BeautifulSoup as bsoup
# We will also need sys to handle argument manipulation
import sys

#This is the main function
#Parameters: item_to_search_for websiteURL1 websiteURL2 etc.
#Parameters are stored as a tuple to parse through
def scrape(arg):
	print "scrape was called with", len(arg), "arguments:",

	for x in arg:
		print x,
	print ""

print "This is the name of the script:", sys.argv[0]
print "Number of arguments:", len(sys.argv)
print "The arguments are:", str(sys.argv)

#This calls the function
#PROBLEM - How to send in the argv values as separate strings???
scrape(list(sys.argv))