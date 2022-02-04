import json
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scrapy import signals
from scrapy_proj.scrapy_proj.spiders.form_meta_spider import FormMetaSpider
from scrapy_proj.scrapy_proj.spiders.big_lottery_spider import BigLotterySpider
from scrapy_proj.scrapy_proj.spiders.gintsai539_spider import Gintsai539Spider
from utils.constant import Game
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from kivymd.app import MDApp


spiders = {
    Game.GINTSAI_539: Gintsai539Spider,
    Game.BIG_LOTTERY: BigLotterySpider,
}


class Crawler:
    def __init__(self, game_key, start_year_month, end_year_month):
        self.game_key = game_key
        self.start_year_month = start_year_month
        self.end_year_month = end_year_month
        self.runner = CrawlerRunner(get_project_settings())
        self.result = []

    def start(self):
        self.__crawl()
        reactor.run()
        self.__sort_result_by_date()

    @defer.inlineCallbacks
    def __crawl(self):
        def callback(signal, sender, item, response, spider):
            self.form_meta = item

        def callback2(signal, sender, item, response, spider):
            self.result.append(item)
            app = MDApp.get_running_app()
            app.info_text += f"getting item: {json.dumps(item)}\n"

        def logging(response, request, spider):
            app = MDApp.get_running_app()
            app.scraped_count += 1

        dispatcher.connect(callback, signal=signals.item_passed)
        yield self.runner.crawl(FormMetaSpider, self.game_key)
        dispatcher.connect(callback2, signal=signals.item_passed)
        dispatcher.connect(logging, signal=signals.response_received)
        yield self.runner.crawl(
            spiders[self.game_key],
            form_meta=self.form_meta,
            start_year_month=self.start_year_month,
            end_year_month=self.end_year_month,
        )
        reactor.stop()

    def __sort_result_by_date(self):
        self.result.sort(
            key=lambda item: int(item["date"][7:])
            + int(item["date"][4:6]) * 31
            + int(item["date"][:3]) * 12 * 31
        )
