import scrapy
from scrapy.http import Request
from utils.constant import CRAWLING_META


class FormMetaSpider(scrapy.Spider):
    name = "form_meta"

    def __init__(self, game_key):
        self.url = CRAWLING_META[game_key]["url"]

    def start_requests(self):
        yield Request(url=self.url)

    def parse(self, response):
        view_state = response.xpath('//*[@id="__VIEWSTATE"]/@value').get()
        view_state_generator = response.xpath(
            '//*[@id="__VIEWSTATEGENERATOR"]/@value'
        ).get()
        event_validation = response.xpath('//*[@id="__EVENTVALIDATION"]/@value').get()

        yield {
            "view_state": view_state,
            "view_state_generator": view_state_generator,
            "event_validation": event_validation,
        }
