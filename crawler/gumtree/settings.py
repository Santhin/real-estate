
BOT_NAME = 'gumtree'
SPIDER_MODULES = ['gumtree.spiders']
NEWSPIDER_MODULE = 'gumtree.spiders'
ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED=True
#Fake user agents
#pip install scrapy-fake-useragent
FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
    'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
]
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

#MongoDB
#pip install scrapy-mongodb
# To ease the load on MongoDB, scrapy-mongodb has a buffering feature. 
# You can enable it by setting MONGODB_BUFFER_DATA to the buffer size you want. E.g: 
# scrapy-mongodb will write 10 documents at a time to the database if you set:

MONGODB_BUFFER_DATA = 20
ITEM_PIPELINES = {
    'scrapy_mongodb.MongoDBPipeline': 300,
}
MONGODB_URI = "connection string inster here"
MONGODB_DATABASE = 'GUMTREE'
MONGODB_COLLECTION = 'mieszkania'


#scrapy-crawl-once
#pip install scrapy-crawl-once

SPIDER_MIDDLEWARES = {
    # ...
    'scrapy_crawl_once.CrawlOnceMiddleware': 100,
    # ...
}

DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_crawl_once.CrawlOnceMiddleware': 50,
    # ...
}


