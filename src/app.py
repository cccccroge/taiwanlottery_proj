from excel_exporter import ExcelExporter
from widgets import RootWidget
from utils.paths import ASSET_FOLDER, KV_FOLDER
from utils.constant import Game
from crawler import Crawler
import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, DictProperty
import os.path
import locale


class MyApp(MDApp):
    game_key = StringProperty(Game.GINTSAI_539)
    time_range = DictProperty({"start": "", "end": ""})

    def build(self):
        # set title
        self.title = "台灣彩券分析"
        # setup locale
        locale.setlocale(locale.LC_TIME, "zh_TW.UTF-8")
        # assign asset path
        kivy.resources.resource_add_path(ASSET_FOLDER)
        # assign kv path
        Builder.load_file(os.path.join(KV_FOLDER, "common.kv"))
        Builder.load_file(os.path.join(KV_FOLDER, "choose_game.kv"))
        Builder.load_file(os.path.join(KV_FOLDER, "choose_range.kv"))
        Builder.load_file(os.path.join(KV_FOLDER, "crawl_and_analyze.kv"))
        Builder.load_file(os.path.join(KV_FOLDER, "root.kv"))
        # dark theme
        self.theme_cls.theme_style = "Dark"

        root = RootWidget()
        # # debug mode
        # inspector.create_inspector(Window, root)

        return root

    def select_game(self, game_key):
        self.game_key = game_key

    def select_range(self, type, value):
        key = "start" if type == "開始時間" else "end"
        self.time_range[key] = value

    def start_crawl_and_analyze(self):
        self.__crawl_to_list()
        self.__create_analyzing_excel()

    def __crawl_to_list(self):
        crawler = Crawler(
            game_key=self.game_key,
            start_year_month=self.time_range["start"].strftime("%Y-%m"),
            end_year_month=self.time_range["end"].strftime("%Y-%m"),
        )
        crawler.start()
        self.list = crawler.result

    def __create_analyzing_excel(self):
        exporter = ExcelExporter(self.list, self.game_key)
        exporter.execute()


if __name__ == "__main__":
    MyApp().run()
