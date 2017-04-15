import requests
import json
import sys

def bestbuy(item):
	try:
	    item
	except NameError:
	    print "item not defined. Reverting to default query."
	    item = "item"
	item = item.replace(" ", "&search=")

	apiKey= "kGSvqQv1lXMAOZG9u6pQGlcg"
	url = "https://api.bestbuy.com/v1/products(search=" + item + ")?format=json&show=url,name,salePrice&apiKey=" + apiKey

	r = requests.get(url)
	j = json.loads(r.text)

	master = []

	for i in range(len(j['products'])):
	    master.append([])
	    master[i].append(j['products'][i]['name'])
	    master[i].append(j['products'][i]['salePrice'])
	    master[i].append(j['products'][i]['url'])

	return master

# for i in bestbuy(sys.argv[1]):
# 	print i[0]
# 	print i[1]
# 	print i[2]