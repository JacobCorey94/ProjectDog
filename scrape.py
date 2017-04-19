import requests
from bs4 import BeautifulSoup as bsoup
import sys
import json
import re
import amazon
import bestbuy
import staples
import macys
import walmart
import homedepot
import target
import newegg
import threading

class Scrape(threading.Thread):
    def __init__(self,target,*args):
        self._target=target
        self._args=args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)

def scrape_wm(arg):
    global master
    try:
        walmartlist = walmart.walmart(arg)
        if walmartlist[0] == "Empty":
                print "Walmart returned no results"
        else:
                master += walmartlist
    except:
        pass
def scrape_target(arg):
    global master
    master += target.target(arg)
def scrape_staples(arg):
    global master
    try:
        st = staples.staples(arg)
        if st[0] == "Empty":
                print "Staples returned no results"
        else:
                master += st
    except:
        pass
def scrape_bb(arg):
    global master
    master += bestbuy.bestbuy(arg)
def scrape_macys(arg):
    macyslist = []
    global master
    try:
        macyslist = macys.macys(arg)
        if macyslist[0] == "Empty":
            print "Macys returned no results"
        else:
            master += macyslist
    except:
        pass
def scrape_homedepot(arg):
    hdl = []
    global master
    try:
        hdl = homedepot.homedepot(arg)
        if hdl[0] == "Empty":
            print "Home Depot returned no results"
        else:
            master += hdl
    except:
        pass
def scrape_amzn(arg):
    amzn = []
    global master
    try:
        amzn = amazon.amazon(arg)
        # amzn[0] = "Empty"
        if amzn[0] == "Empty":
            print "Amazon returned no results"
        else:
            master += amzn
    except:
        pass

def scrape_ne(arg):
    ne = []
    global master
    try:
        ne = newegg.newegg(arg)
        if ne[0] == "Empty":
            print "Newegg returned no results"
        else:
            master += ne
    except:
        pass

def scrape(arg):
    search = arg[1]
    arg.pop(1)
    t = []
    if "amazon" in arg:
        a = Scrape(scrape_amzn, search)
        a.start()
        t.append(a)
    if "bestbuy" in arg:
        bb = Scrape(scrape_bb, search)
        bb.start()
        t.append(bb)
    if "homedepot" in arg:
        hd = Scrape(scrape_homedepot, search)
        hd.start()
        t.append(hd)
    if "macys" in arg:
        m = Scrape(scrape_macys, search)
        m.start()
        t.append(m)
    if "staples" in arg:
        s = Scrape(scrape_staples, search)
        s.start()
        t.append(s)
    if "target" in arg:
        tar = Scrape(scrape_target, search)
        tar.start()
        t.append(tar)
    if "walmart" in arg:
        wm = Scrape(scrape_wm, search)
        wm.start()
        t.append(wm)
    if "newegg" in arg:
        ne = Scrape(scrape_ne, search)
        ne.start()
        t.append(ne)
    for thr in t:
        thr.join()
master = []

#passed = ["scrape.py","nintendo switch","staples","walmart","bestbuy"]
if len(sys.argv) < 3:

    print "ERROR! Wrong arguments passed in, 0.00"
    print "Proper use: python scrape.py item web1 web2 etc, 0.00"
else:
    scrape(list(sys.argv))

print json.dumps(master)
# for i in master:
#     print i[0]
#     print i[1]
#     print i[2]
