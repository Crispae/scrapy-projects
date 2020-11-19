import scrapy
from demo_crawl.items import DemoCrawlItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import  ItemLoader


def apply_priority(priority):
    def process_request(request):
        return request.replace(priority=priority)
    return process_request

class FirstCrawlSpider(CrawlSpider):
    name = 'first_crawl'
    allowed_domains = []
    start_urls = ['https://tutsplus.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="home-hero__column"]/a'),callback='parse_tem',follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='pagination__button pagination__next-button']"),callback='parse_tem',follow=True),
    )

    # def parse_tem(self, response):
    #     yield scrapy.Request(url=response.url,callback=self.extractor,dont_filter=True)

    def parse_tem(self,response):
        #self.logger.info(f'Parsing course page ----->>>{response.url}  ----------->>>> [The request url: {response.request.url}]')
        for path in response.xpath('//li[@class="posts__post  "]/article'):
            loader = ItemLoader(item=DemoCrawlItem(),selector=path,response=response)
            loader.add_xpath("course_name",'.//header/a[2]/h1/text()')
            loader.add_xpath("course_link",'.//header/a/@href')
            loader.add_xpath("course_description",'.//div/text()')
            loader.add_value("userAgent",response.request.headers.get("User-Agent").decode("utf-8"))
            yield loader.load_item()
            
    
    # def parse_category(self, response):
    #     self.logger.info(f'Parsing Home page for link  {response.url} ------->>>[The request url: {response.request}]')


            # item['course__name'] = path.xpath('.//header/a[2]/h1/text()').extract_first()
            # item['course_link'] = path.xpath('.//header/a/@href').extract_first()
            # item['description'] = path.xpath('.//div/text()').extract_first()
            # yield item

        # next_page = response.xpath('//a[@class="pagination__button pagination__next-button"]/@href').extract_first()
        # next_url = response.urljoin(next_page)
        # yield scrapy.Request(next_url,callback=self.parse_tem,dont_filter=True)







    #    yield {"result": f"{requests.get(response.url).text}"}

            # yield scrapy.Request(url=i,callback=self.parse2,dont_filter=True)

    




        # for path in response.xpath('//li[@class="posts__post  "]/article'):
        #     dic ={}
        #     dic['course__name'] = path.xpath('.//header/a[2]/h1/text()').extract_first()
        #     dic['course_link'] = path.xpath('.//header/a/@href').extract_first()
        #     dic['description'] = path.xpath('.//div/text()').extract_first()
        #     return dic

        
