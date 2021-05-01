from datetime import datetime, timedelta
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor
configure_logging()
scheduler = TwistedScheduler(reactor=reactor)
process = CrawlerProcess(get_project_settings())
scheduler.add_job(process.crawl, 'interval', args=['mieszkania'], minutes=15, next_run_time=datetime.now())
#scheduler.add_job(lambda :print('activate'), 'interval', minutes=15, next_run_time=datetime.now() + timedelta(seconds=5))
scheduler.start()
reactor.run()