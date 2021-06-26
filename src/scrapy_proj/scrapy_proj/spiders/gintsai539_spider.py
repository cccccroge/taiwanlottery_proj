import scrapy
from scrapy.http import FormRequest

class Gintsai539Spider(scrapy.Spider):
    name = "gintsai539"

    def start_requests(self):
        url = \
            'https://www.taiwanlottery.com.tw/lotto/DailyCash/history.aspx'
        formdata = {
            'D539Control_history1$dropYear': '110',
            'D539Control_history1$dropMonth': '5',
        }
        return [FormRequest(url=url,
                    formdata=formdata,
                    callback=self.parse)]

    def parse(self, response):
        print(response.body)


        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
