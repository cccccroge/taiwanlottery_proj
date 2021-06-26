import scrapy
from scrapy.http import FormRequest
import os.path

class Gintsai539Spider(scrapy.Spider):
    name = "gintsai539"

    def start_requests(self):
        url = \
            'https://www.taiwanlottery.com.tw/lotto/DailyCash/history.aspx'
        formdata = {
            '__VIEWSTATE': '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',
            '__VIEWSTATEGENERATOR': '09BD3138',
            '__EVENTVALIDATION': 'NUkC6ik0IMpj+gBHudYg7Ln0vN21ejp9z1UHif75ordFAjcxUcHyPufYsOJ3Jsk9NrtOmmu2TxD+VdtJrcLFYfZGipBSHMpB20h4KQZVXoErSNGi6mOzHLWcEazj+IcjTQ36dSRXNQXbUZu048A1OKfT3AgJCG3Dwsfqc1jXfjGkA/yIDfd/G+QWjXd/m1UVnII/MuwKPkVfHZM6d0xMkHuug2VjGDyBAL/JRmaXXfvO/K4hSvO7etG3lb8e+9GFiIgIwYuNRqwPV4l7QxIm+qfpP/PUPN+jtsnC4aa+0iADXtXyhVba8+fGbTa6E7CyPtoUOPcEdDR+MOFubfEzMbJpne90KX1GIsuVp21t4zzk8Z3atoWqdlnVuyxu6fZlEkGkcXIFxpgYdKstUSIUd9SK/WYdRo5cnwrYMlYQq7qpG0Zd8+iUTMRA7i3/YtnEEv6blcvKlRmRdq+3N/f5mYWx2p1Xi1hMFlSUpSGvtWj0yeeuaiDVtfyxIJVqd1P3IJWMqNuqj16MB3BsONrRzExmF6/zJbwTWB90CxWJBYIQQi1AbtF56hMo/EP75uGg81w2OYhtxgvMZ7zJvtIM1t7N4lWz6W24uj0FBFyyjlTcGXLtJWiP0Dq34IP4DLkgQjvw0g==',
            'forma': '請選擇遊戲',
            'D539Control_history1$txtNO': '',
            'D539Control_history1$chk': 'radYM',
            'D539Control_history1$dropYear': '110',
            'D539Control_history1$dropMonth': '5',
            'D539Control_history1$btnSubmit': '查詢',
        }
        return [FormRequest(url=url,
                    formdata=formdata,
                    callback=self.parse)]

    def parse(self, response):
        tables = response.xpath('//*/table[contains(@class, "td_hm")]')

        for t in tables:
            date = t.xpath('.//tr[2]/td[2]/span/span/text()').get()
            num_1 = t.xpath('.//tr[2]/td[4]/span/text()').get()
            num_2 = t.xpath('.//tr[2]/td[5]/span/text()').get()
            num_3 = t.xpath('.//tr[2]/td[6]/span/text()').get()
            num_4 = t.xpath('.//tr[2]/td[7]/span/text()').get()
            num_5 = t.xpath('.//tr[2]/td[8]/span/text()').get()
            yield {
                'date': date,
                'nums': [num_1, num_2, num_3, num_4, num_5],
            }
