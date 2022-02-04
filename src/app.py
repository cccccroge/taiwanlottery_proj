from threading import Thread
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
from kivy.properties import StringProperty, DictProperty, NumericProperty
import os.path
import locale


class MyApp(MDApp):
    game_key = StringProperty(Game.GINTSAI_539)
    time_range = DictProperty({"start": "", "end": ""})

    info_text = StringProperty("")

    total_count = NumericProperty(0)
    scraped_count = NumericProperty(0)

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

        if self.time_range["start"] and self.time_range["end"]:
            d1 = self.time_range["start"]
            d2 = self.time_range["end"]
            self.total_count = (d2.year - d1.year) * 12 + d2.month - d1.month

    def crawl_and_analyze(self):
        crawler = Crawler(
            game_key=self.game_key,
            start_year_month=self.time_range["start"].strftime("%Y-%m"),
            end_year_month=self.time_range["end"].strftime("%Y-%m"),
        )
        crawler.start()
        list = crawler.result
        print(f"total_count: {self.total_count}, scraped_count: {self.scraped_count}")
        exporter = ExcelExporter(list, self.game_key)
        exporter.execute()

    def async_crawl_and_analyze(self):
        thread = Thread(target=self.crawl_and_analyze)
        thread.start()


if __name__ == "__main__":
    MyApp().run()
