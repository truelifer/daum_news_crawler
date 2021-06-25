# Scrapy settings for daum_news_crawler project

BOT_NAME = 'daum_news_crawler'
SPIDER_MODULES = ['daum_news_crawler.spiders']
NEWSPIDER_MODULE = 'daum_news_crawler.spiders'
USER_AGENT = 'daum_news_crawler'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 0
DOWNLOAD_DELAY = 0
RANDOMIZE_DOWNLOAD_DELAY = False

ITEM_PIPELINES = {
   'daum_news_crawler.pipelines.DaumNewsCrawlerPipeline': 300,
}

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = None
LOG_LEVEL = 'INFO'