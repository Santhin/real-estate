import scrapy 
import asyncio
from twisted.internet import asyncioreactor
scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
is_asyncio_reactor_installed = scrapy.utils.reactor.is_asyncio_reactor_installed()
print(f"Is asyncio reactor installed: {is_asyncio_reactor_installed}")
from twisted.internet import reactor
