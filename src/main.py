import subprocess
import os
from utils.paths import SCRAPY_FOLDER, DATA_FOLDER
import json
from openpyxl import Workbook
from utils.constant import GAMES
import numpy as np
from openpyxl.utils import get_column_letter

SETTINGS = {
    'game': GAMES['gin'],
    'start_year_month': '2018-01',
}

def main():
    output_path = os.path.join(DATA_FOLDER, f'{SETTINGS["game"]["key"]}.json')
    # crawl_to_json(output_path, SETTINGS["game"]["key"], SETTINGS["start_year_month"]) \
    #     .wait()
    d = load_and_sort(output_path)
    create_analyzing_excel(d)

def crawl_to_json(output_path, type, start_year_month):
    p = subprocess.Popen([
        'scrapy', 'crawl', type,
        '-O', output_path,
        '-a', f'start_year_month={start_year_month}',
    ], cwd=SCRAPY_FOLDER)
    return p

def load_and_sort(output_path):
    with open(output_path) as f:
        d = json.load(f)
        d.sort(key=lambda item: 
            int(item['date'][7:]) + 
            int(item['date'][4:6]) * 31 + 
            int(item['date'][:3]) * 12 * 31
        )
        return d

def create_analyzing_excel(src_list):
    wb = Workbook()
    construct_sum_sheet(wb, src_list)
    wb.save(os.path.join(DATA_FOLDER, f'{SETTINGS["game"]["label"]}.xlsx'))
    
def construct_sum_sheet(wb, list):
    ws = wb.active
    ws.title = '全部'
    headers = ['日期', *(np.arange(1, 40))]
    ws.append(headers)

    ws.column_dimensions['A'].width = 10
    for i in range(2, 41):
        c = get_column_letter(i)
        ws.column_dimensions[c].width = 3
    
    for item in list:
        row = [item['date'], *(39 * [""])]
        for n in item['nums']:
            row[int(n)] = n
        ws.append(row)
    
    ws.freeze_panes = ws['AO2']


if __name__ == "__main__":
    main()
