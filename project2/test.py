from  w3lib.html import remove_tags

from scrapy.loader.processors import MapCompose, TakeFirst, Join

def qot(value):

    for i in value:
        if (i != "\n") or (i != " "):
            value = i.replace("\n","")
            return value


l = ['\n'
            '      “The trouble with having an open mind, of course, is that '
            'people will insist on coming along and trying to put things in '
            'it.”\n'
            '  ']
print(qot(l))