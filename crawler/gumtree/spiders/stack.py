# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://stackoverflow.com//']
    custom_settings = {
        'EXTENSIONS': {
            'scrapy.extensions.logstats.LogStats': None,
        },
        'TELNETCONSOLE_ENABLED': False,
        'LOG_LEVEL': 'INFO'
    }

    def parse(self, response):
        self.logger.info('parse--------------------------')