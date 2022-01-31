from scrapy_proj.scrapy_proj.spiders import gintsai539_spider, big_lottery_spider

GAMES = {
    'gin': {
        'key': 'gintsai539',
        'spider': gintsai539_spider.Gintsai539Spider,
        'label': '今彩539',
    },
    'big': {
        'key': 'big_lottery',
        'spider': big_lottery_spider.BigLotterySpider,
        'label': '大樂透',
    },
}