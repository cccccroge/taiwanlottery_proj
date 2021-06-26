import subprocess
import os
from utils.paths import SCRAPY_FOLDER, DATA_FOLDER

SETTINGS = {
    'type': 'gintsai539',
    'start_year_month': '2018-01',
}

def main():
    output_path = os.path.join(DATA_FOLDER, f'{SETTINGS["type"]}.json')
    subprocess.run([
        'scrapy', 'crawl', SETTINGS['type'],
        '-O', output_path,
        '-a', f'start_year_month={SETTINGS["start_year_month"]}',
    ], cwd=SCRAPY_FOLDER)

if __name__ == "__main__":
    main()
