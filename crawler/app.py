from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from gumtreev2.spiders.gumtree_crawler import GumtreeCrawler
process = CrawlerProcess(get_project_settings())


process.crawl(GumtreeCrawler)
process.start()