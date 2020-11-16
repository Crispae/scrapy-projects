# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join,Identity
from w3lib.html import remove_tags

def remove_tag(value):
    return remove_tags(value).replace(" ","").replace("\n","")

def qot(value):
    return value.replace(u"\u201c","").replace(u"\u201d","").replace("\n","")



class QuotesItems(scrapy.Item):
    # define the fields for your item here like:
    quotes = scrapy.Field(input_processor = MapCompose(qot),
    output_processor = TakeFirst()
    )

    Author = scrapy.Field(
        input_processor = MapCompose(remove_tag),
        output_processor = TakeFirst()

    )
    Tags = scrapy.Field(
        input_processor = MapCompose(remove_tag),
        output_processor = Join(",")
        
    )
    

