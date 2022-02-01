from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scrapy import signals
from scrapy_proj.scrapy_proj.spiders import form_meta_spider
from scrapy_proj.scrapy_proj.spiders.big_lottery_spider import BigLotterySpider
from scrapy_proj.scrapy_proj.spiders.gintsai539_spider import Gintsai539Spider
from utils.constant import Game
from twisted.internet import reactor, defer


spiders = {
    Game.GINTSAI_539: Gintsai539Spider,
    Game.BIG_LOTTERY: BigLotterySpider,
}


class Crawler:
    def __init__(self, game_key, start_year_month):
        self.game_key = game_key
        self.start_year_month = start_year_month
        self.runner = CrawlerRunner()

    def start(self):
        self.__crawl()
        reactor.run()

    @defer.inlineCallbacks
    def __crawl(self):
        result = []

        def callback(signal, sender, item, response, spider):
            self.form_meta = item

        def callback2(signal, sender, item, response, spider):
            result.append(item)

        dispatcher.connect(callback, signal=signals.item_passed)
        yield self.runner.crawl(form_meta_spider.FormMetaSpider, self.game_key)
        dispatcher.connect(callback2, signal=signals.item_passed)
        yield self.runner.crawl(
            spiders[self.game_key],
            form_meta=self.form_meta,
            start_year_month=self.start_year_month,
        )
        print(result)
        reactor.stop()
