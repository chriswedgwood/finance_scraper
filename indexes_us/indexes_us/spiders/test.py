# -*- coding: utf-8 -*-
import scrapy
import logging


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        logging.debug("*" * 40)
        logging.debug("response text: %s" % response.text)
        logging.debug("response headers: %s" % response.headers)
        logging.debug("request headers: %s" % response.request.headers)
