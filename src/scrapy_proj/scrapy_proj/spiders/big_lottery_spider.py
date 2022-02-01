import scrapy
from scrapy.http import FormRequest
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from utils.date import iter_year_month


class BigLotterySpider(scrapy.Spider):
    name = "big_lottery"

    def __init__(self, start_year_month):
        self.start_year_month = start_year_month
        self.end_year_month = (date.today() + relativedelta(months=1)).strftime("%Y-%m")

    def start_requests(self):
        for (year, month) in iter_year_month(
            self.start_year_month, self.end_year_month
        ):
            url = "https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx"
            formdata = {
                "Lotto649Control_history$txtNO": "",
                "Lotto649Control_history$chk": "radYM",
                "Lotto649Control_history$dropYear": str(year - 1911),
                "Lotto649Control_history$dropMonth": str(month),
                "Lotto649Control_history$btnSubmit": "查詢",
            }
            yield FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        tables = response.xpath('//*/table[contains(@class, "td_hm")]')

        for t in tables:
            date = t.xpath(".//tr[2]/td[2]/span/span/text()").get()
            num_1 = t.xpath(".//tr[5]/td[2]/span/text()").get()
            num_2 = t.xpath(".//tr[5]/td[3]/span/text()").get()
            num_3 = t.xpath(".//tr[5]/td[4]/span/text()").get()
            num_4 = t.xpath(".//tr[5]/td[5]/span/text()").get()
            num_5 = t.xpath(".//tr[5]/td[6]/span/text()").get()
            num_6 = t.xpath(".//tr[5]/td[7]/span/text()").get()
            special_num = t.xpath(".//tr[5]/td[8]/span/span/text()").get()
            yield {
                "date": date,
                "nums": {
                    "normal": [num_1, num_2, num_3, num_4, num_5, num_6],
                    "special": [special_num],
                },
            }
