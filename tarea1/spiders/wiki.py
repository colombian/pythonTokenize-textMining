# -*- coding: utf-8 -*-
import scrapy
from tarea1.items import Tarea1Item


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Portal:Biography']

    def parse(self, response):
        for article in response.css('div.div-col ul li a::attr(href)').extract():
            #print('https://en.wikipedia.org'+article)
            yield scrapy.Request('https://en.wikipedia.org'+article, callback=self.parse_article)
            #yield scrapy.Request(url, callback=self.parse_page)
        
    def parse_article(self, response):
        article = Tarea1Item()
        titleArt = response.css('h1::text').extract()  
        corpus = response.css('p').xpath('string()').extract()
        subjects = list()
        for title in response.css('h2 span.mw-headline'):
            subjects.append(title.attrib['id'])
        
        article['Title'] = titleArt
        article['Subjects'] = subjects
        article['Corpus'] = corpus
        
        yield article
        
        
