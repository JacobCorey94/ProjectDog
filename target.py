import requests
import json
import sys

def target(item):
    try:
        item
    except NameError:
        print "item not defined. Reverting to default query."
        item = "item"
    item = item.replace(" ", "+")

    url = "http://redsky.target.com/v1/plp/search?keyword="+item+"&count=24&offset=0&sort_by=relevance"
   
    r = requests.get(url)
    j = json.loads(r.text)

    master = []

    for i in range(len(j['search_response']['items']['Item'])):
        master.append([])
        master[i].append(j['search_response']['items']['Item'][i]['title'])
        master[i].append(j['search_response']['items']['Item'][i]['list_price']['price'])
        master[i].append("www.target.com" + j['search_response']['items']['Item'][i]['url'])

    return master

print target("target")
