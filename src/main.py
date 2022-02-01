from excel_exporter import ExcelExporter
from utils.constant import Game
from crawler import Crawler


def main():
    game_key = Game.BIG_LOTTERY
    l = crawl_to_list(game_key)
    create_analyzing_excel(l, game_key)


def crawl_to_list(game_key):
    crawler = Crawler(game_key=game_key, start_year_month="2018-07")
    crawler.start()
    return crawler.result


def create_analyzing_excel(list, game_key):
    exporter = ExcelExporter(list, game_key)
    exporter.execute()


if __name__ == "__main__":
    main()
