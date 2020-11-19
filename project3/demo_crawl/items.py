# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join,Identity


class DemoCrawlItem(scrapy.Item):

    # define the fields for your item here like:
    course_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    course_link = scrapy.Field(

        output_processor = TakeFirst()
    )
    course_description = scrapy.Field(
        output_processor = TakeFirst()
    )
    userAgent = scrapy.Field(
        output_processor = TakeFirst()
    )

