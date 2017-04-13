from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sample.items import SampleItem

class MySpider(BaseSpider):
        name = "test"
        allowed_domains = ["craigslist.org"]
        start_urls = ["https://tallahassee.craigslist.org/search/ofc"]

        def parse(self, response):
            hxs = HtmlXPathSelector(response)
            titles = hxs.select("//p")
            items = []
            for titles in titles:
                    item = SampleItem()
                    item ["title"] = titles.select("a/text()").extract()
                    item ["link"] = titles.select("a/@href").extract()
                    items.append(item)
            
            return items
