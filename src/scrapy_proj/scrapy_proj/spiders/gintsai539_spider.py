import scrapy
from scrapy.http import FormRequest
from datetime import date
from dateutil.relativedelta import relativedelta
from utils.constant import CRAWLING_META, Game
from utils.date import iter_year_month


class Gintsai539Spider(scrapy.Spider):
    def __init__(self, form_meta, start_year_month):
        self.form_meta = {**form_meta, **CRAWLING_META[Game.GINTSAI_539]}
        self.start_year_month = start_year_month
        self.end_year_month = (date.today() + relativedelta(months=1)).strftime("%Y-%m")

    def start_requests(self):
        for (year, month) in iter_year_month(
            self.start_year_month, self.end_year_month
        ):
            url = self.form_meta["url"]
            formdata = {
                "__VIEWSTATE": self.form_meta["view_state"],
                "__VIEWSTATEGENERATOR": self.form_meta["view_state_generator"],
                "__EVENTVALIDATION": self.form_meta["event_validation"],
                f"{self.form_meta['form_prefix']}$txtNO": "",
                f"{self.form_meta['form_prefix']}$chk": "radYM",
                f"{self.form_meta['form_prefix']}$dropYear": str(
                    year - 1911
                ),
                f"{self.form_meta['form_prefix']}$dropMonth": str(
                    month
                ),
                f"{self.form_meta['form_prefix']}$btnSubmit": "查詢",
            }
            yield FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        tables = response.xpath('//*/table[contains(@class, "td_hm")]')

        for t in tables:
            date = t.xpath(".//tr[2]/td[2]/span/span/text()").get()
            num_1 = t.xpath(".//tr[2]/td[4]/span/text()").get()
            num_2 = t.xpath(".//tr[2]/td[5]/span/text()").get()
            num_3 = t.xpath(".//tr[2]/td[6]/span/text()").get()
            num_4 = t.xpath(".//tr[2]/td[7]/span/text()").get()
            num_5 = t.xpath(".//tr[2]/td[8]/span/text()").get()
            yield {
                "date": date,
                "nums": [num_1, num_2, num_3, num_4, num_5],
            }
