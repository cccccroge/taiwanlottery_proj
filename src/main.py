import subprocess
import os
from utils.paths import SCRAPY_FOLDER

def main():
    print(SCRAPY_FOLDER)
    os.chdir(SCRAPY_FOLDER)
    subprocess.run(['scrapy', 'crawl', 'gintsai539', '-O', 'test.json'])

if __name__ == "__main__":
    main()
