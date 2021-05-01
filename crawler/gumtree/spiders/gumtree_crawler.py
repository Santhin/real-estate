import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GumtreeCrawler(CrawlSpider):
    name = 'mieszkania'
    #download_delay = 2.0
    allowed_domains = ['www.gumtree.pl']
    def my_request_processor(request, response):
        request.meta['crawl_once'] = True
        return request

    def start_requests(self):
        yield scrapy.Request(url='https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/warszawa/v1c9073l3200008p1')

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='href-link tile-title-text']"),
             callback='parse_item', follow=True, process_request=my_request_processor),
        Rule(LinkExtractor(
            restrict_xpaths="//a[@class='arrows icon-right-arrow icon-angle-right-gray']"))
    )


    def parse_item(self, response):

        yield {
            "tytuł": response.xpath("//span[@class='myAdTitle']/text()").get(),
            "opis": response.xpath((".//div[@class='description']/span/p[string(.)]/text() | .//div[@class='description']/span[@class='pre']/text() |.//div[@class='description']/span[@class='pre']/div/text() | .//div[@class='description']/span/p/text() | .//div[@class='description']/span/div/p/text() | .//div[@class='description']/span/div/div/text() | .//div[@class='description']/span/b/text() | .//div[@class='description']/span/div/i/b/text() | .//div[@class='description']/span/p/b/text() | //div[@class='vip-details']/div[@class='description']/span/text() | .//div[@class='description']/span/i/text()")).getall(),
            "cena": response.xpath("//span[@class='amount']/text()[1]").get(),
            ##Tabelka:
            "data dodania": response.xpath(".//div[@class='attribute' and contains(span, 'Data dodania')]/span[2]/text()").get(),
            "lokalizacja":  response.xpath(".//div[@class='attribute' and contains(span, 'Lokalizacja')]/span[2]/div/a/text()").getall(),
            "Na_sprzedaż_przez":  response.xpath(".//div[@class='attribute' and contains(span, 'Na sprzedaż przez')]/span[2]/text()").getall(),
            "Rodzaj_nieruchomosci":  response.xpath(".//div[@class='attribute' and contains(span, 'Rodzaj nieruchomości')]/span[2]/text()").getall(),
            "Liczba_pokoi":  response.xpath(".//div[@class='attribute' and contains(span, 'Liczba pokoi')]/span[2]/text()").getall(),
            "Liczba_łazienek":  response.xpath(".//div[@class='attribute' and contains(span, 'Liczba łazienek')]/span[2]/text()").getall(),
            "Wielkość (m2)":  response.xpath(".//div[@class='attribute' and contains(span, 'Wielkość (m2)')]/span[2]/text()").getall(),
            "Parking":  response.xpath(".//div[@class='attribute' and contains(span, 'Parking')]/span[2]/text()").getall(),
            "mieszkanie_url" : response.url,
            ## Dane techniczne
            "User-Agent": (response.request.headers['User-Agent']).decode(),
            "Proxy": response.meta

        }
