from excel_exporter import ExcelExporter
from utils.paths import ASSET_FOLDER, KV_FOLDER
from utils.constant import Game
from crawler import Crawler
import kivy
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.picker import MDDatePicker
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
import os.path
import locale


class RootWidget(ScreenManager):
    pass


class NextStep(AnchorLayout):
    def slide_to_next(self):
        sm = MDApp.get_running_app().root
        names = sm.screen_names
        idx = names.index(sm.current_screen.name)
        next_idx = (idx + 1) % len(names)
        sm.current = names[next_idx]


class GameButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light


class DateInput(MDTextField):
    def open_date_picker(self):
        picker = MDDatePicker(
            title="選擇時間",
            title_input="輸入時間",
            font_name="font/Noto_Sans_TC/NotoSansTC-Bold.otf",
        )
        picker.bind(on_save=self.on_save)
        picker.open()

    def on_focus(self, instance, value):
        if value:
            super().on_focus(instance, value)
            self.open_date_picker()

    def on_save(self, instance, value, date_range):
        self.text = value.strftime("%Y-%m-%d")


class MyApp(MDApp):
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
        Builder.load_file(os.path.join(KV_FOLDER, "root.kv"))

        # dark theme
        self.theme_cls.theme_style = "Dark"

        root = RootWidget()

        # debug mode
        inspector.create_inspector(Window, root)

        return root


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
