# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import os



class Project2Pipeline:


    def create_db(self):
        conn = sqlite3.connect("quotes.db")
        curr = conn.cursor()

        curr.execute(""" CREATE TABLE quotes(

            Author text,
            Quotes text,
            Tags   text
        )""")

        conn.commit()
        conn.close()
        
    def process_item(self, item, spider):

        if len(item.keys()) == 3:


    
        
            data = [item["Author"],item["quotes"],item["Tags"],]

        
            if os.path.isfile("quotes.db"):
                conn = sqlite3.connect("quotes.db")
                curr = conn.cursor()

                curr.execute(""" INSERT INTO quotes VALUES(?,?,?)""",data)
                conn.commit()
            else:
                self.create_db()
                conn = sqlite3.connect("quotes.db")
                curr = conn.cursor()

                curr.executemany(""" INSERT INTO quotes VALUES(?,?,?)""",data)
                conn.commit()


            return item
