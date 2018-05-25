# -*- coding: utf-8 -*-
import scrapy
from ..items import EstadaoItem
from urllib.parse import urlparse

class EstadaoSpider(scrapy.Spider):
    name = 'estadao'
    allowed_domains = ['www.politica.estadao.com.br',
                        'www.economia.estadao.com.br',
                        'www.internacional.estadao.com.br']
    start_urls = ['http://politica.estadao.com.br/',
                  'http://economia.estadao.com.br',
                  'https://internacional.estadao.com.br']

    def parse(self, response):
        urls = response.xpath('//a[contains(@href, "/noticias/")]/@href').extract()
        urls = [x for x in urls if self.get_domain(x) in self.allowed_domains]
        for url in list(set(urls)):
            print("Processing... " + url)

    def get_domain(self, url):
        parsed_uri = urlparse(url)
        domain = 'www.{uri.netloc}'.format(uri=parsed_uri)
        return domain
