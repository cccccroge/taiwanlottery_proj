from excel_exporter import ExcelExporter
from utils.paths import ASSET_FOLDER, KV_FOLDER
from utils.constant import Game
from crawler import Crawler
import kivy

kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
import os.path


class RootWidget(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        self.title = "台灣彩券分析"
        kivy.resources.resource_add_path(ASSET_FOLDER)
        Builder.load_file(os.path.join(KV_FOLDER, "step_layout.kv"))
        Builder.load_file(os.path.join(KV_FOLDER, "root.kv"))

        return RootWidget()


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
    MyApp().run()
