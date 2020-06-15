
import scrapy


class Tarea1Item(scrapy.Item):
    # Get from articles
    Title = scrapy.Field()
    Subjects = scrapy.Field()
    Corpus = scrapy.Field()
