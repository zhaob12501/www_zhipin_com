# -*- coding: utf-8 -*-

# Scrapy settings for www_zhipin_com project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'www_zhipin_com'

SPIDER_MODULES = ['www_zhipin_com.spiders']
NEWSPIDER_MODULE = 'www_zhipin_com.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'www_zhipin_com (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'lastCity=101010100; t=ihwwU9HNfhcMv2Qs; wt=ihwwU9HNfhcMv2Qs; JSESSIONID=""; __c=1522995715; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1522486111,1522494470,1522583104,1522995715; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1522995874; __a=66639934.1512268251.1522583104.1522995715.274.35.7.213',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831",
    'dnt': "1",
    'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
    'upgrade-insecure-requests': "1",

}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'www_zhipin_com.middlewares.WwwZhipinComSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'www_zhipin_com.middlewares.WwwZhipinComDownloaderMiddleware': 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    'www_zhipin_com.middlewares.ProxyMiddleWare': 125,
#}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'www_zhipin_com.pipelines.WwwZhipinComPipeline': 300,
#}

#ITEM_PIPELINES = {
#    'www_zhipin_com.pipelines.WwwZhipinComPipeline': 300,
#}
ITEM_PIPELINES = {
    'www_zhipin_com.pipelines.WwwZhipinComPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_ENABLED = True

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
FEED_EXPORT_ENCODING = 'utf-8'
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
# MONGO_URI = 'mongodb://localhost:27017/'
# MONGO_DATABASE = 'iApp'
# CLOSESPIDER_ITEMCOUNT = 300

# scrapy crawl fast -s CLOSESPIDER_ITEMCOUNT=10
# scrapy crawl fast -s CLOSESPIDER_PAGECOUNT=10
# scrapy crawl fast -s CLOSESPIDER_TIMEOUT=10
