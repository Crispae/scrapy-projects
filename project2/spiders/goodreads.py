import scrapy
from project2.items import QuotesItems
from scrapy.loader import ItemLoader

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    def start_requests(self):


        
        allowed_domains = ['https://www.goodreads.com/']
        start_urls = ['https://www.goodreads.com/quotes?page=1/']

        yield scrapy.Request(url = start_urls[0],callback=self.parse)
    
    def parse(self, response):
        for quote in response.selector.xpath("//div/*[@class='quote']"):
            loader = ItemLoader(item=QuotesItems(),selector=quote,response=response)
            loader.add_xpath("quotes",".//div/*[@class='quoteText']/text()[1]")
            loader.add_xpath("Author",".//span[@class='authorOrTitle']")
            loader.add_xpath("Tags",'.//div[@class="greyText smallText left"]/a')
            yield loader.load_item()
            


        next_page = response.selector.xpath('//a[@class="next_page"]/@href').extract_first() # extract_first() return only string
        if next_page is not None:
            next_pageurl = response.urljoin(next_page)

            yield scrapy.Request(next_pageurl,callback= self.parse)


#quotes xpath = ".//div/*[@class='quoteText']/text()[1]"
#author = ".//span[@class='authorOrTitle']/text()" ## .//div[@class='quoteText']/child::span/text()
#tags = './/div[@class="greyText smallText left"]/a/text()'
