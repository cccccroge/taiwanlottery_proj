from utils.constant import Game
from crawler import Crawler
from excel_exporter import create_analyzing_excel


def main():
    l = crawl_to_list()
    create_analyzing_excel(l)


def crawl_to_list():
    crawler = Crawler(game_key=Game.GINTSAI_539, start_year_month="2021-12")
    crawler.start()
    return crawler.result


if __name__ == "__main__":
    main()
