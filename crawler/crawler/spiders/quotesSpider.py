import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import  CrawlerItem
from scrapy.loader import ItemLoader


class quotesSpider(CrawlSpider):
    name = 'bright_network_jobs'
    allowed_domains = ["brightnetwork.co.uk"]
    start_urls = ['https://www.brightnetwork.co.uk/graduate-jobs/']

    rules = (
        Rule(LinkExtractor(allow=(r'search_position=')) , callback="parse_item"),
        Rule(LinkExtractor(allow=(r'graduate-jobs')))

    )

    def parse_item(self, response):
        bLoader = ItemLoader(item = CrawlerItem() , response=response)
        bLoader.add_css("name" , "h1.tw-mb-6")
        bLoader.add_css("tag" , "a.tw-pill")
        bLoader.add_css("description" , "article")

        return bLoader.load_item()
        
        
        
        
        
        
        
        ''' 
        name: response.css("h1.tw-mb-6::text").get()
        tag:  response.css("a.tw-pill::text").get()
        content:  response.css("article ::text").extract()
        '''
